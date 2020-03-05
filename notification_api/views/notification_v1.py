from flask import request, Blueprint, Response, current_app
from notifications_python_client.errors import HTTPError
from notification_api.exceptions import ApplicationError
from flask_negotiate import consumes, produces
from jsonschema import validate, ValidationError
import json

# This is the blueprint object that gets registered into the app in blueprints.py.
notification_v1 = Blueprint('notification_v1', __name__)

# JSON schema for notification requests
with open('notification_api/swagger.json') as json_file:
    swagger = json.load(json_file)

notification_schema = swagger["definitions"]["PostNotificationRequest"]


@notification_v1.route("/notifications", methods=["POST"])
@consumes("application/json")
@produces('application/json')
def notifications():
    notification_request = request.json

    # Validate request against schema
    try:
        validate(notification_request, notification_schema)
    except ValidationError as e:
        raise ApplicationError(str(e), "E001", 400)

    try:
        if "email_address" in notification_request:
            notification = current_app.notifications_client.send_email_notification(
                email_address=notification_request["email_address"],
                template_id=notification_request["template_id"],
                personalisation=notification_request["personalisation"],
                reference=notification_request["reference"]
            )

        elif "phone_number" in notification_request:
            notification = current_app.notifications_client.send_sms_notification(
                phone_number=notification_request["phone_number"],
                template_id=notification_request["template_id"],
                personalisation=notification_request["personalisation"],
                reference=notification_request["reference"]
            )
            
    except HTTPError as e:
        raise ApplicationError(e.message, e.status_code, e.status_code)
    else:
        response = Response(response=json.dumps(notification, separators=(',', ':')),
                            mimetype='application/json',
                            status=201)
        response.headers["Location"] = notification["uri"]

        return response


@notification_v1.route("/notifications/<uuid:notification_id>", methods=["GET"])
@produces('application/json')
def notification(notification_id):
    try:
        notification = current_app.notifications_client.get_notification_by_id(notification_id)
    except HTTPError as e:
        raise ApplicationError(e.message, e.status_code, e.status_code)
    else:

        return Response(response=json.dumps(notification, separators=(',', ':')),
                        mimetype='application/json',
                        status=200)
