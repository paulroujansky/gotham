"""
This file contains low-level CRUD operations for the Gotham API.
It defines functions for creating, reading, updating, and deleting crimes in the database.
Business logic should be handled in the service layer.
"""

from typing import List, Optional

import psycopg2
import os

from gotham.core.models import Crime

SQL_DIR = os.path.join(os.path.dirname(__file__), "..", "sql", "crimes")


def load_sql(filename: str) -> str:
    with open(os.path.join(SQL_DIR, filename), "r") as f:
        return f.read()


SELECT_BY_ID_SQL = load_sql("select_by_id.sql")
SELECT_ALL_SQL = load_sql("select_all.sql")
INSERT_SQL = load_sql("insert.sql")
UPDATE_SQL = load_sql("update.sql")
DELETE_SQL = load_sql("delete.sql")


def get_crime(conn: psycopg2.extensions.connection, crime_id: int) -> Optional[Crime]:
    """
    Fetch a specific crime by ID from the database.

    Args:
        conn: Database connection
        crime_id: ID of the crime to retrieve

    Returns:
        Crime object if found, None otherwise
    """
    with conn.cursor() as cursor:
        cursor.execute(SELECT_BY_ID_SQL, {"crime_id": crime_id})
        row = cursor.fetchone()
        return Crime.from_db_row(row) if row else None


def get_crimes(
    conn: psycopg2.extensions.connection, skip: int = 0, limit: int = 100
) -> List[Crime]:
    """
    Fetch a list of crimes with pagination from the database.

    Args:
        conn: Database connection
        skip: Number of records to skip
        limit: Maximum number of records to return

    Returns:
        List of Crime objects
    """
    with conn.cursor() as cursor:
        cursor.execute(SELECT_ALL_SQL, {"limit": limit, "skip": skip})
        rows = cursor.fetchall()
        return [Crime.from_db_row(row) for row in rows]


def create_crime(conn: psycopg2.extensions.connection, crime: Crime) -> Crime:
    """
    Insert a new crime into the database.

    Args:
        conn: Database connection
        crime: Crime object to create

    Returns:
        Created Crime object with ID
    """
    with conn.cursor() as cursor:
        cursor.execute(
            INSERT_SQL,
            {
                "type": crime.type,
                "description": crime.description,
                "location": crime.location,
                "suspect_name": crime.suspect_name,
                "date_time": crime.date_time,
                "latitude": crime.latitude,
                "longitude": crime.longitude,
            },
        )
        row = cursor.fetchone()
        conn.commit()
        return Crime.from_db_row(row)


def update_crime(
    conn: psycopg2.extensions.connection, crime_id: int, crime: Crime
) -> Optional[Crime]:
    """
    Update an existing crime in the database.

    Args:
        conn: Database connection
        crime_id: ID of the crime to update
        crime: Updated Crime object

    Returns:
        Updated Crime object if found, None otherwise
    """
    with conn.cursor() as cursor:
        cursor.execute(
            UPDATE_SQL,
            {
                "type": crime.type,
                "description": crime.description,
                "location": crime.location,
                "suspect_name": crime.suspect_name,
                "date_time": crime.date_time,
                "latitude": crime.latitude,
                "longitude": crime.longitude,
                "crime_id": crime_id,
            },
        )
        row = cursor.fetchone()
        conn.commit()
        return Crime.from_db_row(row) if row else None


def delete_crime(conn: psycopg2.extensions.connection, crime_id: int) -> bool:
    """
    Delete a crime from the database.

    Args:
        conn: Database connection
        crime_id: ID of the crime to delete

    Returns:
        True if the crime was deleted, False if it wasn't found
    """
    with conn.cursor() as cursor:
        cursor.execute(DELETE_SQL, {"crime_id": crime_id})
        row = cursor.fetchone()
        conn.commit()
        return row is not None
