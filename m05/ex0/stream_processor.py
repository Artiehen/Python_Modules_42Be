from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"

    def run(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Validation failed")

            result = self.process(data)
            return self.format_output(result)

        except Exception as error:
            return f"[ERROR] {error}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:
            _ = sum(data)
            return True
        except TypeError:
            return False

    def process(self, data: Any) -> str:
        print("Initializing Numeric Processor...")
        print(f"Processing Data: {data}")
        print("Validation: Numeric data verified")
        x = f"Processed {len(data)} numeric values:"
        return f"{x} sum={sum(data)}, avg={sum(data) / len(data)}\n"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:
            data.split()
            return True
        except AttributeError:
            return False

    def process(self, data: Any) -> str:
        print("Initializing Text Processor...")
        print(f"Processing data: {data}")
        print("Validation: Text data verified")
        x = "Processed text: "
        return f"{x}{len(data)} characters {len(data.split())} words\n"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:
            _ = data["name"]
            _ = data["reason"]
            _ = data["status"]
            return True
        except (TypeError, KeyError):
            return False

    def process(self, data: Any) -> str:
        print("Initializing Log Processor...")
        print(f"Processing data: {data['name']} {data['reason']}")
        print("Validation: Log entry verified")
        y = f"[{data["status"]}] {data["name"]}"
        x = f"{y} level detected: {data["reason"]}"
        return f"{x}"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    try:
        num_processor = NumericProcessor()
        nums = [1, 2, 3, 4, 5]
        data = num_processor.run(nums)
        print(data)

    except (ValueError, TypeError, NameError) as e:
        print(e)

    try:
        str_processor = TextProcessor()
        txt = "Hello Nexus World"
        data = str_processor.run(txt)
        print(data)

    except (ValueError, TypeError) as e:
        print(e)

    try:
        log_processor = LogProcessor()
        log = {"name": "ERROR", "reason": "Connection timeout",
               "status": "ALERT"}
        data = log_processor.run(log)
        print(data)

    except (ValueError, TypeError, NameError) as e:
        print(e)

    try:
        processors = [
            NumericProcessor(),
            TextProcessor(),
            LogProcessor()
        ]

        data_samples = [
            [1, 2, 3],
            "Polymorphism without is great!",
            {"name": "INFO", "reason": "System ready", "status": "INFO"}
        ]
        print("\n=== Polymorphic Processing Demo ===\n")

        for i in range(len(processors)):
            processor = processors[i]
            data = data_samples[i]
            print(processor.run(data))

        print("\nFoundation systems online. Nexus ready for advanced streams.")

    except (ValueError, TypeError, NameError) as e:
        print(e)


if __name__ == "__main__":
    main()
