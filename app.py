# app.py



from flask import Flask


from iam.interfaces.services import iam_api
from telemetry.interfaces.services import telemetry_api

import iam.application.services

from shared.infrastructure.database import init_db

# --- Flask Application Initialization ---
app = Flask(__name__)


app.register_blueprint(iam_api)
app.register_blueprint(telemetry_api)


first_request = True


@app.before_request
def setup():

    global first_request
    if first_request:
        first_request = False

        print("--- First Request Setup: Initializing System ---")

        init_db()
        print("[OK] Database initialized and tables created.")

        auth_application_service = iam.application.services.AuthApplicationService()
        device = auth_application_service.get_or_create_test_device()

        print(f"[OK] Test device '{device.device_id}' is ready.")
        print(f"     => Use this API Key in your client: '{device.api_key}'")

        print("-------------------------------------------------")
        print("Edge service is now running and ready for requests.")
        print("-------------------------------------------------")




# --- Main Execution Block ---
if __name__ == "__main__":


    app.run(host='0.0.0.0', port=5000, debug=True)