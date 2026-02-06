from abc import ABC, abstractmethod
from typing import Any


class DataStream(ABC):

    @abstractmethod
    def process_batch():
        pass


class SensorStream(DataStream):
    pass


class TransactionStream(DataStream):
    pass


class EventStream(DataStream):
    pass


class StreamProcessor:
    pass


def main():
    print("")


if __name__ == "__main__":
    main()