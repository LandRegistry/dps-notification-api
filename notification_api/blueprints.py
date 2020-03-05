# Import every blueprint file
from notification_api.views import general, notification_v1


def register_blueprints(app):
    """Adds all blueprint objects into the app."""
    app.register_blueprint(general.general)
    app.register_blueprint(notification_v1.notification_v1, url_prefix='/v1')

    # All done!
    app.logger.info("Blueprints registered")
