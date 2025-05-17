"""
Data models for the Gotham API.
"""

from datetime import datetime
from typing import Any, Dict, Optional, Tuple

from robyn.openapi import Body


class CrimeBody(Body):
    type: str
    description: str
    location: str
    suspect_name: str
    date_time: str  # Changed from datetime to str for OpenAPI compatibility
    latitude: float
    longitude: float


class Crime:
    """
    Represents a crime in Gotham City.
    """

    def __init__(
        self,
        type: str,
        description: str,
        location: str,
        suspect_name: str,
        date_time: datetime,
        latitude: float,
        longitude: float,
        id: Optional[int] = None,
    ):
        self.id = id
        self.type = type
        self.description = description
        self.location = location
        self.suspect_name = suspect_name
        self.date_time = date_time
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def from_db_row(cls, row: Optional[Tuple[Any, ...]]) -> Optional["Crime"]:
        """
        Create a Crime instance from a database row.

        Args:
            row: Database row tuple

        Returns:
            Crime instance if row exists, None otherwise
        """
        if not row:
            return None
        return cls(
            id=row[0],
            type=row[1],
            description=row[2],
            location=row[3],
            suspect_name=row[4],
            date_time=row[5],
            latitude=row[6],
            longitude=row[7],
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Crime instance to a dictionary.

        Returns:
            Dictionary representation of the Crime
        """
        return {
            "id": self.id,
            "type": self.type,
            "description": self.description,
            "location": self.location,
            "suspect_name": self.suspect_name,
            "date_time": self.date_time.isoformat() if self.date_time else None,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }
