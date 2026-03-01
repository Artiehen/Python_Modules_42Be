from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import Optional


class ContacType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContacType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    is_verified: bool = True
    message_received: Optional[str] = Field(default=None, max_length=500)

    @model_validator(mode="after")
    def val_bus_rules(self):
        ct1 = "Telepathic contact must have at least 3 witnesses"
        ct4 = "Strong signals (> 7.0) should include received messages"
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type == ContacType.physical and not self.is_verified:
            raise ValueError("Must verify physical contact")
        if (
            self.contact_type == ContacType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(ct1)
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(ct4)
        return self


def main():
    try:
        print("Alien Contact Log Validation")
        print("=" * 50)

        valid_data = {
            "contact_id": "AC_2024_001",
            "timestamp": "2024-01-22",
            "location": "Area 51, Nevada",
            "contact_type": "radio",
            "signal_strength": 8.5,
            "duration_minutes": 45,
            "witness_count": 5,
            "is_verified": True,
            "message_received": "'Greetings from Zeta Reticuli'"
            }

        contact = AlienContact(**valid_data)
        print("Valid contact report")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnessess: {contact.witness_count}")
        print(f"Message: {contact.message_received}\n")
        print("=" * 50)

    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))

    try:
        invalid_data = valid_data.copy()
        invalid_data["contact_id"] = "AC_2024_001"
        invalid_data["contact_type"] = "telepathic"
        invalid_data["witness_count"] = 2
        AlienContact(**invalid_data)
    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
