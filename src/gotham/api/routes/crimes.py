"""
Crime-related routes for the Gotham API.
"""

import json

from robyn import Request, SubRouter

from gotham.api.responses import error_response, json_response
from gotham.core import crud
from gotham.core.models import Crime, CrimeBody
from gotham.services import crime_service

crime_router = SubRouter(__file__, prefix="/crimes")


@crime_router.get("/")
async def get_crimes(request: Request):
    """
    Get a list of crimes with pagination.

    Args:
        request: Request object

    Returns:
        List of Crime objects
    """
    skip = int(request.query_params.get("skip", "0"))
    limit = int(request.query_params.get("limit", "100"))

    crimes = crime_service.list_crimes(skip=skip, limit=limit)

    return json_response({"crimes": [crime.to_dict() for crime in crimes]})


@crime_router.get("/:crime_id")
async def get_crime(request: Request):
    """
    Get a specific crime by ID.

    Args:
        request: Request object

    Returns:
        Crime object
    """
    crime_id = int(request.path_params.get("crime_id"))

    crime = crime_service.get_crime_by_id(crime_id)

    if crime is None:
        return error_response("Crime not found", 404)

    return json_response(crime.to_dict())


@crime_router.post("/")
async def add_crime(request: Request, body: CrimeBody):
    """
    Add a new crime.

    Args:
        request: Request object
        body: CrimeBody object

    Returns:
        Created crime object
    """
    crime_data = json.loads(body)
    crime = Crime(**crime_data)

    crime = crime_service.create_crime_service(crime)

    return json_response(
        {"message": "Crime added successfully", "crime": crime.to_dict()}, status=201
    )


@crime_router.put("/:crime_id")
async def update_crime(request: Request, body: CrimeBody):
    """
    Update an existing crime.

    Args:
        request: Request object
        body: CrimeBody object

    Returns:
        Updated crime object
    """
    crime_id = int(request.path_params.get("crime_id"))
    crime_data = json.loads(body)
    crime = Crime(**crime_data)

    updated_crime = crime_service.update_crime_service(crime_id, crime)

    if updated_crime is None:
        return error_response("Crime not found", 404)

    return json_response(
        {"message": "Crime updated successfully", "crime": updated_crime.to_dict()}
    )


@crime_router.delete("/:crime_id")
async def delete_crime(request: Request):
    """
    Delete a crime by ID.

    Args:
        request: Request object

    Returns:
        Message indicating the crime was deleted
    """
    crime_id = int(request.path_params.get("crime_id"))
    success = crime_service.delete_crime_service(crime_id)

    if not success:
        return error_response("Crime not found", 404)

    return json_response({"message": "Crime deleted successfully"}, status=204)
