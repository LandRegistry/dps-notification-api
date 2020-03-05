# Notification API

## Dependencies
* [GOV.UK Notify API](https://github.com/alphagov/notifications-api) - via [notifications python client](https://github.com/alphagov/notifications-python-client)

## Specification

This API is defined using [OpenAPI Specification 2.0](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) compliant [`swagger.json`](notification_api/swagger.json) code.

## Examples

### Create notification

#### Email

Request: `POST /v1/notifications`
```json
{
  "email_address":"@digital.landregistry.gov.uk",
  "template_id":"123456789-123456789",
  "personalisation":{
    "name":"Matthew"
  },
  "reference":null
}

```

Response: `201`
```json
{
    "content": {
        "from_email": "data.publication.service@notifications.service.gov.uk",
        "subject": "Test Message from DPS Beta",
        "body": "Hello Matthew, \r\n\r\nThis is a test email from the DPS service."
    },
    "id": "c03eb8fb-a87e-4cb6-bd07-123456789",
    "template": {
        "version": 1,
        "uri": "https://api.notifications.service.gov.uk/services/89ad4221-dd11-423f-b725-123456789/templates/c8b58621-79e7-4ce1-a87f-ef6dde87a7e0",
        "id": "c8b58621-79e7-4ce1-a87f-ef6dde87a7e0"
    },
    "uri": "https://api.notifications.service.gov.uk/v2/notifications/c03eb8fb-a87e-4cb6-bd07-123456789",
    "reference": null,
    "scheduled_for": null
}
```

#### SMS

Request: `POST /v1/notifications`
```json
{
  "phone_number":"07890123456",
  "template_id":"123456789-123456789",
  "personalisation":{
    "first_name":"Test",
    "last_name":"User"
  },
  "reference":null
}
```

Response: `201`
```json
{
  "uri": "https://api.notifications.service.gov.uk/v2/notifications/123456",
  "content": {
    "body": "Hello Test user",
    "from_number": "HMLR"
  },
  "template": {
    "uri": "https://api.notifications.service.gov.uk/services",
    "version": 3,
    "id": "a156f411-bfc7-47f5-8081-232d6eab409c"
  },
  "id": "ce878f7f-e644-4b0d-9f7d-c6a1696ceb58",
  "reference": null
}
```

### Get notification

#### Email

Request: `GET /v1/notifications/6d2b37b2-481b-4777-b3e3-123456789`

Response: `200`
```json
{
    "id": "c03eb8fb-a87e-4cb6-bd07-123456789",
    "subject": "Test Message from DPS Beta",
    "template": {
        "version": 1,
        "uri": "https://api.notifications.service.gov.uk/v2/template/c8b58621-79e7-4ce1-a87f-123456789/version/1",
        "id": "c8b58621-79e7-4ce1-a87f-123456789"
    },
    "line_3": null,
    "line_2": null,
    "postcode": null,
    "phone_number": null,
    "status": "delivered",
    "created_by_name": null,
    "email_address": "@digital.landregistry.gov.uk",
    "completed_at": "2018-11-20T11:52:02.816996Z",
    "reference": null,
    "scheduled_for": null,
    "line_5": null,
    "created_at": "2018-11-20T11:52:00.721886Z",
    "sent_at": "2018-11-20T11:52:01.607479Z",
    "type": "email",
    "line_6": null,
    "line_4": null,
    "body": "Hello Matthew, \r\n\r\nThis is a test email from the DPS service.",
    "postage": null,
    "line_1": null
}
```

#### SMS

Request `GET /v1/notifications/ce878f7f-e644-4b0d-9f7d-123456789`

Response: `200`
```json
{
  "body": "Hello Test user",
  "line_4": null,
  "template": {
    "uri": "https://api.notifications.service.gov.uk/service",
    "version": 3,
    "id": "a156f411-bfc7-47f5-8081-123456789"
  },
  "subject": null,
  "status": "delivered",
  "line_1": null,
  "sent_at": "2017-03-13T15:52:45.066343Z",
  "postcode": null,
  "type": "sms",
  "phone_number": "+447890123456",
  "email_address": null,
  "id": "ce878f7f-e644-4b0d-9f7d-123456789",
  "completed_at": "2017-03-13T15:52:45.109140Z",
  "created_at": "2017-03-13T15:52:43.624314Z",
  "line_6": null,
  "reference": null,
  "line_3": null,
  "line_2": null,
  "line_5": null
}
```

## Error Codes
* E005 - Failed to send email notification.
* E006 - Failed to send SMS notification.
* E007 - Failed to get notification.

## Skeleton Documentation

This app is derived from the Flask Skeleton API, for further documentation please refer to the [README](http://192.168.249.38/skeletons/flask-skeleton-api/blob/master/README.md).

## Further Documentation

This application is further documented on [TechDocs](http://192.168.250.79/index.php/Notifications).
