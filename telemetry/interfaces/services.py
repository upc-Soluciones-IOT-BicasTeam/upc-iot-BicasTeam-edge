

from flask import Blueprint, request, jsonify
from telemetry.application.services import TelemetryRecordApplicationService
from iam.interfaces.services import authenticate_request  # Re-use the authentication function
from datetime import datetime  # Import datetime for formatting

telemetry_api = Blueprint("telemetry_api", __name__)

telemetry_app_service = TelemetryRecordApplicationService()


@telemetry_api.route("/api/v1/telemetry/records", methods=["POST"])
def create_telemetry_record():
    """
    API endpoint to create a new telemetry record.
    It expects a JSON payload and an 'X-API-Key' header.

    Endpoint: POST /api/v1/telemetry/records
    """
    auth_result = authenticate_request()
    if auth_result:
        return auth_result

    data = request.json
    try:
        sensor_data = data.get("sensor_data", {})
        gps_data = data.get("gps_data", {})

        new_record = telemetry_app_service.create_telemetry_record(
            api_key=request.headers.get("X-API-Key"),
            device_id=data["device_id"],
            temp=sensor_data.get("temperature"),
            hum=sensor_data.get("humidity"),
            lat=gps_data.get("latitude"),
            lon=gps_data.get("longitude"),
            alt=gps_data.get("altitude_meters", 0.0),
            spd=gps_data.get("speed_kmph", 0.0),
            timestamp=gps_data.get("timestamp_utc")
        )

        print("-------------------------------------------------")
        print(f"✅ Telemetry Record Saved (ID: {new_record.id})")
        print(f"   Device:      {new_record.device_id}")
        print(f"   Timestamp:   {new_record.recorded_at.strftime('%Y-%m-%d %H:%M:%S')} UTC")
        print(f"   Temperature: {new_record.temperature:.2f} °C")
        print(f"   Humidity:    {new_record.humidity:.1f} %")
        print(f"   Location:    Lat: {new_record.latitude}, Lon: {new_record.longitude}")
        print(f"   Speed:       {new_record.speed:.2f} km/h")
        print("-------------------------------------------------")

        return jsonify({
            "message": "Telemetry record created successfully.",
            "record": {
                "id": new_record.id,
                "device_id": new_record.device_id,
                "recorded_at": new_record.recorded_at.isoformat()
            }
        }), 201

    except KeyError as e:
        return jsonify({"error": f"Missing required field in JSON payload: {e}"}), 400
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400