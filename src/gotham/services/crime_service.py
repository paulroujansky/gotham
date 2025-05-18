"""
Service layer for crime-related business logic in the Gotham API.
This module orchestrates CRUD operations and is the place for validation, transformation, and other business rules.
"""

from typing import List, Optional

from gotham.core.models import Crime
from gotham.core import crud
from gotham.db.database import get_db_connection


def get_crime_by_id(crime_id: int) -> Optional[Crime]:
    """Retrieve a crime by its ID.

    Args:
        crime_id (int): The ID of the crime to retrieve.

    Returns:
        Optional[Crime]: The crime if found, else None.
    """
    with get_db_connection() as conn:
        return crud.get_crime(conn, crime_id)


def list_crimes(skip: int = 0, limit: int = 100) -> List[Crime]:
    """List crimes with pagination.

    Args:
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to return.

    Returns:
        List[Crime]: List of crimes.
    """
    with get_db_connection() as conn:
        return crud.get_crimes(conn, skip=skip, limit=limit)


def create_crime_service(crime: Crime) -> Crime:
    """Create a new crime record.

    Args:
        crime (Crime): The crime to create.

    Returns:
        Crime: The created crime with ID.
    """
    # Place for validation or transformation if needed
    with get_db_connection() as conn:
        return crud.create_crime(conn, crime)


def update_crime_service(crime_id: int, crime: Crime) -> Optional[Crime]:
    """Update an existing crime record.

    Args:
        crime_id (int): The ID of the crime to update.
        crime (Crime): The updated crime data.

    Returns:
        Optional[Crime]: The updated crime if found, else None.
    """
    with get_db_connection() as conn:
        return crud.update_crime(conn, crime_id, crime)


def delete_crime_service(crime_id: int) -> bool:
    """Delete a crime by its ID.

    Args:
        crime_id (int): The ID of the crime to delete.

    Returns:
        bool: True if deleted, False if not found.
    """
    with get_db_connection() as conn:
        return crud.delete_crime(conn, crime_id)
