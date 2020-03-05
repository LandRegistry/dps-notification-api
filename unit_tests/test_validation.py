from notification_api.main import app
import unittest
import json
import copy


class TestValidation(unittest.TestCase):
    """
        This test case is to test that all the required fields in the are being sent to `/notifications` route.

        No need to mock anything because when the validation works a 400 request is returned and nothing
        is written to the database.
    """

    def setUp(self):
        self.app = app.test_client()
        self.example_email = {"email_address": "test@digital.landregistry.gov.uk",
                              "template_id": "123456789-123456789",
                              "personalisation": {"first_name": "Test",
                                                  "last_name": "User",
                                                  "token": "!s3kpRIC$MYmox0!"},
                              "reference": None}
        self.example_sms = {"phone_number": "07890123456",
                            "template_id": "123456789-123456789",
                            "personalisation": {"first_name": "Test",
                                                "last_name": "User"},
                            "reference": None}

    def test_email(self):
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        data = copy.deepcopy(self.example_email)

        # data specifically shouldn't contain a email_address for this test
        data.pop("email_address")

        response = self.app.post('/v1/notifications', headers=headers, data=json.dumps(data))

        self.assertEqual(response.status_code, 400)
        assert("Failed validating 'oneOf' in schema:" in response.data.decode("utf-8"))
        assert("{'required': ['email_address']}") in response.data.decode("utf-8")

    def test_sms(self):
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        data = copy.deepcopy(self.example_sms)

        # data specifically shouldn't contain a email_address for this test
        data.pop("phone_number")

        response = self.app.post('/v1/notifications', headers=headers, data=json.dumps(data))

        self.assertEqual(response.status_code, 400)
        assert("Failed validating 'oneOf' in schema:" in response.data.decode("utf-8"))
        assert("{'required': ['phone_number']}") in response.data.decode("utf-8")

    def test_template(self):
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        data = copy.deepcopy(self.example_email)

        # data specifically shouldn't contain a template_id for this test
        data.pop("template_id")

        response = self.app.post('/v1/notifications', headers=headers, data=json.dumps(data))

        self.assertEqual(response.status_code, 400)
        assert("'template_id' is a required property" in response.data.decode("utf-8"))

    def test_personalisation(self):
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        data = copy.deepcopy(self.example_email)

        # data specifically shouldn't contain a personalisation for this test
        data.pop("personalisation")

        response = self.app.post('/v1/notifications', headers=headers, data=json.dumps(data))

        self.assertEqual(response.status_code, 400)
        assert("'personalisation' is a required property" in response.data.decode("utf-8"))
