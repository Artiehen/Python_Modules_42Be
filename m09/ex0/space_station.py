from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    try:
        print("Space Station Data Validation")
        print("=" * 50)
        x = "Status: "
        op = "Operational"
        valid_data = {"station_id": "ISS001",
                      "name": "International Space Station",
                      "crew_size": 6,
                      "power_level": 85.5,
                      "oxygen_level": 92.3,
                      "last_maintenance": "1992-05-22",
                      "is_operational": False,
                      "notes": None
                      }
        station = SpaceStation(**valid_data)
        print("Valid Station Created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"crew: {station.crew_size}")
        print(f"Power: {station.power_level}")
        print(f"Oxygen: {station.oxygen_level}")
        print(f'{x}{op if station.is_operational else "Not operational"}\n')
        print("=" * 50)
        print("Expected validation error:")
    except Exception as e:
        print(e)
    try:
        invalid_data = valid_data.copy()
        invalid_data["crew_size"] = 22
        SpaceStation(**invalid_data)
    except Exception as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
