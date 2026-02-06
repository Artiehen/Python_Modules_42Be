from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


class DataStream(ABC):
    """
    Abstract base class for all data streams.
    """

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.processed_batches = 0
        self.total_items = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data.
        Must be implemented by subclasses.
        """
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Default filtering behavior.
        Subclasses may override.
        """
        if criteria is None:
            return data_batch

        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Default statistics for a stream.
        """
        return {
            "stream_id": self.stream_id,
            "processed_batches": self.processed_batches,
            "total_items": self.total_items
        }


class SensorStream(DataStream):
    """
    Stream for numeric sensor data.
    """

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            numeric_data = [float(x) for x in data_batch]
        except (TypeError, ValueError):
            raise ValueError("SensorStream requires numeric data")

        self.processed_batches += 1
        self.total_items += len(numeric_data)

        average = sum(numeric_data) / len(numeric_data)
        return f"Sensor average: {average:.2f}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "SensorStream"
        return stats


class TransactionStream(DataStream):
    """
    Stream for transaction data.
    Expected format: {'amount': float, 'type': str}
    """

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            amounts = [item["amount"] for item in data_batch]
        except (TypeError, KeyError):
            raise ValueError("Invalid transaction data format")

        self.processed_batches += 1
        self.total_items += len(amounts)

        total = sum(amounts)
        return f"Total transaction amount: {total:.2f}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch

        return [
            tx for tx in data_batch
            if tx.get("type") == criteria
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "TransactionStream"
        return stats


class EventStream(DataStream):
    """
    Stream for event messages.
    """

    def process_batch(self, data_batch: List[Any]) -> str:
        if not all(isinstance(event, str) for event in data_batch):
            raise ValueError("EventStream requires string events")

        self.processed_batches += 1
        self.total_items += len(data_batch)

        return f"Processed {len(data_batch)} events"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch

        return [
            event for event in data_batch
            if event.lower().startswith(criteria.lower())
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "EventStream"
        return stats


class StreamProcessor:
    """
    Manages and processes multiple streams polymorphically.
    """

    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_streams(
        self,
        batches: Dict[str, List[Any]],
        criteria: Optional[str] = None
    ):
        for stream in self.streams:
            try:
                data_batch = batches.get(stream.stream_id, [])
                filtered = stream.filter_data(data_batch, criteria)
                result = stream.process_batch(filtered)
                print(f"[{stream.stream_id}] {result}")
            except Exception as error:
                print(f"[{stream.stream_id}] ERROR: {error}")

    def print_stats(self):
        for stream in self.streams:
            print(stream.get_stats())


def main():
    sensor_stream = SensorStream("sensor_1")
    transaction_stream = TransactionStream("tx_1")
    event_stream = EventStream("event_1")

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    mixed_batches = {
        "sensor_1": [22.5, 21.8, 23.1],
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
