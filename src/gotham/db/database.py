"""
Database connection management for the Gotham API.
"""

import contextlib
from typing import Generator

import psycopg2
from psycopg2.extensions import connection

from gotham.config import settings


@contextlib.contextmanager
def get_db_connection() -> Generator[connection, None, None]:
    """
    Get a database connection.

    Yields:
        Database connection
    """
    conn = psycopg2.connect(
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASS,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
    )
    try:
        yield conn
    finally:
        conn.close()
