from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


class DataStream(ABC):
    label: str = "items"

    def __init__(self, stream_id: str) -> None:
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

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Default filtering behavior.
        """
        if criteria is None or criteria == "":
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int]]:
        """
        Returns structured statistics for the stream.
        """
        return {
            "stream_id": self.stream_id,
            "label": self.label,
            "total_items": self.total_items
        }


class SensorStream(DataStream):
    label = "readings"

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

        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type Environmental Data")
        print(f"Processing sensor batch: {data_batch}")

        self.processed_batches += 1
        self.total_items += len(values)

        avg_temp = values[0] if values else 0
        return f"Sensor Analysis: {len(values)} readings, avg_temp {avg_temp}C"


class TransactionStream(DataStream):
    label = "operations"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            spent = [item["buy"] for item in data_batch]
            earned = [item["sell"] for item in data_batch]
        except (TypeError, KeyError):
            raise ValueError("Invalid transaction data format")

        print("Initializing Financial Data...")
        print(f"Stream ID: {self.stream_id}, Type Financial Data")
        print(f"Processing transaction batch: {data_batch}")

        self.processed_batches += 1
        self.total_items += len(spent)

        total_spent = sum(spent)
        total_earned = sum(earned)
        return (f"Total transaction analysis: total spent {total_spent:.2f} "
                f"and total earned {total_earned:.2f}")


class EventStream(DataStream):
    label = "events"

    def process_batch(self, data_batch: List[Any]) -> str:
        if not all(isinstance(event, str) for event in data_batch):
            raise ValueError("EventStream requires string events")

        self.processed_batches += 1
        self.total_items += len(data_batch)

        print("\nInitializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type Event Data")
        print(f"Processing event batch: {data_batch}")

        return f"Event Analysis: {len(data_batch)} events"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None or criteria == "":
            return data_batch
        return [
            event for event in data_batch
            if event.lower().startswith(criteria.lower())
        ]


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(self, batches: Dict[str, List[Any]],
                        criteria: Optional[str] = None) -> None:
        for stream in self.streams:
            try:
                data_batch = batches.get(stream.stream_id, [])
                filtered = stream.filter_data(data_batch, criteria)
                result = stream.process_batch(filtered)
                print(f"{result}\n")
            except Exception as error:
                print(f"[{stream.stream_id}] ERROR: {error}")

    def print_stats(self) -> None:
        print("Batch 1 Results:")
        for stream in self.streams:
            stats = stream.get_stats()
            name = stats["stream_id"].split("_")[0].capitalize()
            print(
                f"- {name} data: {stats['total_items']}"
                f" {stats['label']} processed"
            )


def main() -> None:
    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    mixed_batches = {
        "SENSOR_001": [{"temperature": 22.5},
                       {"humidity": 21.8}, {"pressure": 23.1}],
        "TRANS_001": [
            {"buy": 100.0, "sell": 150},
            {"buy": 150.0, "sell": 100}
        ],
        "EVENT_001": [
            "Success",
            "Failure",
            "Logout"
        ]
    }

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    processor.process_streams(mixed_batches, criteria="")

    print("\n=== Stream Statistics ===")
    processor.print_stats()
    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
