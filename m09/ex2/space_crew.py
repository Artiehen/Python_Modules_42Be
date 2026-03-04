from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime


class CrewRank(str, Enum):
    cadet = "cadet"
    office = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    location: str = Field(min_length=3, max_length=100)
    rank: CrewRank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def val_bus_rules(self) -> str:
        ct1 = "Crew not experienced enough, must be +5 years"
        ct2 = "All crew members must be active for this mission!"

        # Mission ID must start with M
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # Must have at least one commander or captain
        if not any(member.rank in [CrewRank.captain, CrewRank.commander]
                   for member in self.crew):
            raise ValueError("Mission must have one Commander or Captain")

        # Long missions require experienced crew
        if self.duration_days >= 365:
            if any(member.years_experience < 5 for member in self.crew):
                raise ValueError(ct1)

        # All crew must be active
        if any(not member.is_active for member in self.crew):
            raise ValueError(ct2)

        return self


def main() -> None:
    try:
        valid_mission = {
            "mission_id": "M2024_MARS",
            "mission_name": "Mars Colony Establishment",
            "destination": "Mars",
            "launch_date": "2024-01-22",
            "duration_days": 900,
            "crew": [
                {
                    "member_id": "M001",
                    "name": "Sarah Connor",
                    "location": "Onboard",
                    "rank": "commander",
                    "age": 50,
                    "specialization": "Mission Command",
                    "years_experience": 30,
                    "is_active": True
                    },
                {
                    "member_id": "M002",
                    "name": "John Smith",
                    "location": "Onboard",
                    "rank": "lieutenant",
                    "age": 45,
                    "specialization": "Navigation",
                    "years_experience": 15,
                    "is_active": True
                    },
                {
                    "member_id": "M003",
                    "name": "Alice Johnson",
                    "location": "Onboard",
                    "rank": "officer",
                    "age": 44,
                    "specialization": "Engineering",
                    "years_experience": 10,
                    "is_active": True
                    }
                ],
            "mission_status": "Active",
            "budget_millions": 2500.0
            }
        mission = SpaceMission(**valid_mission)
        print("Space Mission Crew Validation")
        print("=" * 50)
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: {mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for crew in mission.crew:
            print(f'- {crew.name} ({crew.rank}) - {crew.specialization}')
        print("\n", "=" * 50)

    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))
    try:
        invalid_mission = valid_mission.copy()
        # invalid_mission["mission_id"] = "AC_2024_001"
        invalid_mission["crew"] = [
                {
                    "member_id": "M001",
                    "name": "Sarah Connor",
                    "location": "Onboard",
                    "rank": "cadet",
                    "age": 50,
                    "specialization": "Mission Command",
                    "years_experience": 30,
                    "is_active": True
                    },
                {
                    "member_id": "M002",
                    "name": "John Smith",
                    "location": "Onboard",
                    "rank": "lieutenant",
                    "age": 45,
                    "specialization": "Navigation",
                    "years_experience": 1,
                    "is_active": True
                    },
                {
                    "member_id": "M003",
                    "name": "Alice Johnson",
                    "location": "Onboard",
                    "rank": "officer",
                    "age": 44,
                    "specialization": "Engineering",
                    "years_experience": 10,
                    "is_active": False
                    }
                ]
        invalid_mission["witness_count"] = 2
        SpaceMission(**invalid_mission)
    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
