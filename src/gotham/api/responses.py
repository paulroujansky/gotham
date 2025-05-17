"""
Response helper functions for the Gotham API.
"""

import json
from typing import Any, Dict, Tuple
from robyn import Headers, Response


def json_response(
    data: Any, status: int = 200
) -> Tuple[Dict[str, Any], Dict[str, Any], int]:
    """
    Create a standardized JSON response.

    Args:
        data: Response data
        headers: Headers to include in the response
        status: HTTP status code

    Returns:
        Tuple of (response data, headers, status code)
    """
    return Response(
        description=json.dumps(data),
        headers=Headers({"Content-Type": "application/json"}),
        status_code=status,
    )


def error_response(
    message: str, status: int = 400
) -> Tuple[Dict[str, Any], Dict[str, Any], int]:
    """
    Create a standardized error response.

    Args:
        message: Error message
        headers: Headers to include in the response
        status: HTTP status code

    Returns:
        Tuple of (error data, headers, status code)
    """
    return Response(
        description=json.dumps({"error": message}),
        headers=Headers({"Content-Type": "application/json"}),
        status_code=status,
    )
