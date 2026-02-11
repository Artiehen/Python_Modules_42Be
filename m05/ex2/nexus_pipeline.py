from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol
import time


# ==========================
# Processing Stage Protocol
# ==========================

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


# ==========================
# Concrete Processing Stages
# ==========================

class InputStage:
    def process(self, data: Any) -> Any:
        print("InputStage: Receiving data...")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        print("TransformStage: Transforming data...")

        if isinstance(data, list):
            return [str(item).upper() for item in data]

        if isinstance(data, dict):
            return {k: str(v).upper() for k, v in data.items()}

        return str(data).upper()


class OutputStage:
    def process(self, data: Any) -> Any:
        print("OutputStage: Finalizing output...")
        return data


# ==========================
# Abstract Pipeline Base
# ==========================

class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.execution_time: float = 0.0
        self.processed_items: int = 0
        self.failed: bool = False

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def execute_stages(self, data: Any) -> Any:
        try:
            start_time = time.time()

            for stage in self.stages:
                data = stage.process(data)

            self.execution_time = time.time() - start_time

            if isinstance(data, list):
                self.processed_items += len(data)
            else:
                self.processed_items += 1

            return data

        except Exception as error:
            self.failed = True
            print(f"[{self.pipeline_id}] ERROR in stage execution: {error}")
            return None

    def get_stats(self) -> Dict[str, Union[str, int, float, bool]]:
        return {
            "pipeline_id": self.pipeline_id,
            "execution_time": round(self.execution_time, 5),
            "processed_items": self.processed_items,
            "failed": self.failed
        }


# ==========================
# Manual JSON Adapter
# ==========================

class JSONAdapter(ProcessingPipeline):

    def simple_json_parse(self, data: str) -> Dict[str, Any]:
        """
        VERY simplified JSON parser:
        Only works for flat JSON objects like:
        {"key": "value", "num": "123"}
        """

        data = data.strip().strip("{}")
        pairs = data.split(",")

        result: Dict[str, Any] = {}

        for pair in pairs:
            if ":" not in pair:
                continue
            key, value = pair.split(":", 1)

            key = key.strip().strip('"').strip("'")
            value = value.strip().strip('"').strip("'")

            result[key] = value

        return result

    def simple_json_dump(self, data: Dict[str, Any]) -> str:
        items = []
        for k, v in data.items():
            items.append(f'"{k}": "{v}"')
        return "{ " + ", ".join(items) + " }"

    def process(self, data: Any) -> Union[str, Any]:
        print(f"[{self.pipeline_id}] JSONAdapter processing... {data}")

        if not isinstance(data, str):
            self.failed = True
            return None

        try:
            parsed = self.simple_json_parse(data)
            result = self.execute_stages(parsed)
            return self.simple_json_dump(result)
        except Exception as error:
            print(f"[{self.pipeline_id}] JSON processing failed: {error}")
            self.failed = True
            return None


# ==========================
# Manual CSV Adapter
# ==========================

class CSVAdapter(ProcessingPipeline):

    def process(self, data: Any) -> str:
        print(f"[{self.pipeline_id}] StreamAdapter processing... {data}")
        return self.execute_stages(data)


# ==========================
# Stream Adapter
# ==========================

class StreamAdapter(ProcessingPipeline):

    def process(self, data: Any) -> Union[str, Any]:
        print(f"[{self.pipeline_id}] StreamAdapter processing... {data}")
        return self.execute_stages(data)


# ==========================
# Nexus Manager
# ==========================

class NexusManager:

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def run_all(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        results: Dict[str, Any] = {}

        for pipeline in self.pipelines:
            data = inputs.get(pipeline.pipeline_id)
            if data is None:
                continue

            print(f"\n=== Running Pipeline: {pipeline.pipeline_id} ===")
            results[pipeline.pipeline_id] = pipeline.process(data)

        return results

    def print_stats(self) -> None:
        print("\nCODE NEXUS SUMARRY")
        for pipeline in self.pipelines:
            stats = pipeline.get_stats()
            name = stats["pipeline_id"].split("_")[0].capitalize()
            print(
                f"- {name} data: {stats['processed_items']} processed items in"
                f" {stats['execution_time']} S"
            )


# ==========================
# Demonstration
# ==========================

def main() -> None:

    print("=== CODE NEXUS - NO JSON/CSV MODULE VERSION ===\n")

    json_pipeline = JSONAdapter("json_pipeline")
    csv_pipeline = CSVAdapter("csv_pipeline")
    stream_pipeline = StreamAdapter("stream_pipeline")

    for pipeline in [json_pipeline, csv_pipeline, stream_pipeline]:
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())

    manager = NexusManager()
    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    inputs = {
        "json_pipeline": '{"sensor": "temp", "value": "23.5", "unit": "C"}',
        "csv_pipeline": "user,action3,timestamp",
        "stream_pipeline": ["event1", "event2", "event3"]
    }

    results = manager.run_all(inputs)

    print("\n=== Results ===")
    for key, value in results.items():
        print(f"{key}: {value}")

    manager.print_stats()


if __name__ == "__main__":
    main()
