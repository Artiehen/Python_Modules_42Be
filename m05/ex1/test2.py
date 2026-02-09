from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


# ===================== BASE CLASS =====================

class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_batches = 0
        self.total_items = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        # Default: no filtering unless overridden
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.stream_id,
            "processed_batches": self.processed_batches,
            "total_items": self.total_items
        }


# ===================== SENSOR STREAM =====================

class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "No sensor data"

        try:
            values: List[float] = []

            for item in data_batch:
                for key in ("temperature", "humidity", "pressure"):
                    if key in item:
                        values.append(float(item[key]))

        except (TypeError, ValueError):
            raise ValueError("SensorStream requires numeric sensor values")

        self.processed_batches += 1
        self.total_items += len(values)

        average = sum(values) / len(values)
        return f"Sensor average: {average:.2f}"

    def get_stats(self) -> Dict[str, Union[str, int]]:
        stats = super().get_stats()
        stats["type"] = "SensorStream"
        return stats


# ===================== TRANSACTION STREAM =====================

class TransactionStream(DataStream):

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [tx for tx in data_batch if tx.get("type") == criteria]

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "No transactions after filtering"

        try:
            amounts = [float(tx["amount"]) for tx in data_batch]
        except (TypeError, KeyError, ValueError):
            raise ValueError("Invalid transaction data format")

        self.processed_batches += 1
        self.total_items += len(amounts)

        total = sum(amounts)
        return f"Total transaction amount: {total:.2f}"

    def get_stats(self) -> Dict[str, Union[str, int]]:
        stats = super().get_stats()
        stats["type"] = "TransactionStream"
        return stats


# ===================== EVENT STREAM =====================

class EventStream(DataStream):

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch

        return [
            event for event in data_batch
            if isinstance(event, str)
            and event.lower().startswith(criteria.lower())
        ]

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "No events after filtering"

        if not all(isinstance(event, str) for event in data_batch):
            raise ValueError("EventStream requires string events")

        self.processed_batches += 1
        self.total_items += len(data_batch)

        return f"Processed {len(data_batch)} events"

    def get_stats(self) -> Dict[str, Union[str, int]]:
        stats = super().get_stats()
        stats["type"] = "EventStream"
        return stats


# ===================== STREAM PROCESSOR =====================

class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(
        self,
        batches: Dict[str, List[Any]],
        criteria: Optional[str] = None
    ) -> None:
        for stream in self.streams:
            try:
                data_batch = batches.get(stream.stream_id, [])
                filtered = stream.filter_data(data_batch, criteria)
                result = stream.process_batch(filtered)

                print(f"[{stream.stream_id}] {result}")

            except Exception as error:
                print(f"[{stream.stream_id}] ERROR: {error}")

    def print_stats(self) -> None:
        for stream in self.streams:
            print(stream.get_stats())


# ===================== MAIN =====================

def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_stream = SensorStream("sensor_1")
    transaction_stream = TransactionStream("tx_1")
    event_stream = EventStream("event_1")

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    mixed_batches = {
        "sensor_1": [
            {"temperature": 22.5},
            {"humidity": 21.8},
            {"pressure": 23.1}
        ],
        "tx_1": [
            {"amount": 100.0, "type": "credit"},
            {"amount": 50.0, "type": "debit"},
            {"amount": 75.0, "type": "credit"}
        ],
        "event_1": [
            "LoginSuccess",
            "LoginFailure",
            "Logout"
        ]
    }

    print("=== Processing Streams ===")
    processor.process_streams(mixed_batches, criteria="credit")

    print("\n=== Stream Statistics ===")
    processor.print_stats()


if __name__ == "__main__":
    main()
