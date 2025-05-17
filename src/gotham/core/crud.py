"""
This file contains the CRUD operations for the Gotham API.
It defines the functions for creating, reading, updating, and deleting crimes.
"""

from typing import List, Optional

import psycopg2

from gotham.core.models import Crime


def get_crime(conn: psycopg2.extensions.connection, crime_id: int) -> Optional[Crime]:
    """
    Get a specific crime by ID.

    Args:
        conn: Database connection
        crime_id: ID of the crime to retrieve

    Returns:
        Crime object if found, None otherwise
    """
    with conn.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, type, description, location, suspect_name, date_time, latitude, longitude
            FROM crimes
            WHERE id = %s
            """,
            (crime_id,),
        )
        row = cursor.fetchone()
        return Crime.from_db_row(row) if row else None


def get_crimes(
    conn: psycopg2.extensions.connection, skip: int = 0, limit: int = 100
) -> List[Crime]:
    """
    Get a list of crimes with pagination.

    Args:
        conn: Database connection
        skip: Number of records to skip
        limit: Maximum number of records to return

    Returns:
        List of Crime objects
    """
    with conn.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT id, type, description, location, suspect_name, date_time, latitude, longitude
            FROM crimes
            ORDER BY date_time DESC
            LIMIT {limit} OFFSET {skip}
            """,
        )
        rows = cursor.fetchall()
        return [Crime.from_db_row(row) for row in rows]


def create_crime(conn: psycopg2.extensions.connection, crime: Crime) -> Crime:
    """
    Create a new crime.

    Args:
        conn: Database connection
        crime: Crime object to create

    Returns:
        Created Crime object with ID
    """
    with conn.cursor() as cursor:
        cursor.execute(
            f"""
            INSERT INTO crimes (type, description, location, suspect_name, date_time, latitude, longitude)
            VALUES ('{crime.type}', '{crime.description}', '{crime.location}', '{crime.suspect_name}', '{crime.date_time}', {crime.latitude}, {crime.longitude})
            RETURNING id, type, description, location, suspect_name, date_time, latitude, longitude
            """
        )
        row = cursor.fetchone()
        conn.commit()
        return Crime.from_db_row(row)


def update_crime(
    conn: psycopg2.extensions.connection, crime_id: int, crime: Crime
) -> Optional[Crime]:
    """
    Update an existing crime.

    Args:
        conn: Database connection
        crime_id: ID of the crime to update
        crime: Updated Crime object

    Returns:
        Updated Crime object if found, None otherwise
    """
    with conn.cursor() as cursor:
        cursor.execute(
            f"""
            UPDATE crimes
            SET type = '{crime.type}',
                description = '{crime.description}',
                location = '{crime.location}',
                suspect_name = '{crime.suspect_name}',
                date_time = '{crime.date_time}',
                latitude = {crime.latitude},
                longitude = {crime.longitude}
            WHERE id = {crime_id}
            RETURNING id, type, description, location, suspect_name, date_time, latitude, longitude
            """
        )
        row = cursor.fetchone()
        conn.commit()
        return Crime.from_db_row(row) if row else None


def delete_crime(conn: psycopg2.extensions.connection, crime_id: int) -> bool:
    """
    Delete a crime.

    Args:
        conn: Database connection
        crime_id: ID of the crime to delete

    Returns:
        True if the crime was deleted, False if it wasn't found
    """
    with conn.cursor() as cursor:
        cursor.execute(
            f"""
            DELETE FROM crimes
            WHERE id = {crime_id}
            RETURNING id
            """,
        )
        row = cursor.fetchone()
        conn.commit()
        return row is not None
