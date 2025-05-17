"""
This is the main file for the Gotham API.
It initializes the application and registers routes.
"""

from robyn import Robyn
from robyn.openapi import OpenAPI, OpenAPIInfo

from gotham.api.routes.crimes import crime_router
from gotham.config import settings

# Initialize the app
app = Robyn(
    __file__,
    openapi=OpenAPI(
        info=OpenAPIInfo(
            title=settings.APP_TITLE,
            description=settings.APP_DESCRIPTION,
            version=settings.package_version,
        ),
    ),
)

# Register routes
app.include_router(crime_router)
app.add_response_header("Content-Type", "application/json")


if __name__ == "__main__":
    app.start(host=settings.APP_HOST, port=settings.APP_PORT)
