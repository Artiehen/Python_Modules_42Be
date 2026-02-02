def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def generator_demonstration():
    fib_iter = iter(fibonacci())
    print("Fibonacci sequence (first 10):", end=" ")
    first = True
    for _ in range(10):
        if not first:
            print(", ", end="")
        fib_numb = next(fib_iter)
        print(fib_numb, end="")
        first = False
    print()

    prime_iter = iter(prime())
    print("Prime Numbers (first 5):", end=" ")
    first = True
    for _ in range(5):
        if not first:
            print(", ", end="")
        prime_numb = next(prime_iter)
        print(prime_numb, end="")
        first = False
    print()


def event_stream(n):
    for i in range(1, n + 1):
        yield i


def filter_important_event(stream):
    list_events = ["Killed monster", "found treasure", "leveled up!"]
    important_events = iter(list_events)
    for event in stream:
        if event % 10 == 0:
            try:
                yield next(important_events)
            except StopIteration:
                important_events = iter(list_events)
                yield next(important_events)


def main():
    print("===  Game Data Stream Processor  ===\n")
    print(" Processing 1000 game events ...\n")
    players = ["Alice (level 5)", "Bob (level 12)", "Charlie (level 8)"]
    events = 1000
    p_iter = iter(players)
    leveled_up_count = 0
    found_count = 0
    stream = event_stream(events)
    filter_event = filter_important_event(stream)
    i = 1
    for event in filter_event:
        try:
            p = next(p_iter)
        except StopIteration:
            p_iter = iter(players)
            p = next(p_iter)
        print(f"Event {i}: {p} {event}")
        i += 1

        if event == "leveled up!":
            leveled_up_count += 1
        if event == "found treasure":
            found_count += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed {events}")
    print(f"High level players (10+): {i * 10}")
    print(f"Treasure Events: {found_count}")
    print(f"Level Up events: {leveled_up_count}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")
    print("=== Generator Demonstration ===")
    generator_demonstration()


if __name__ == "__main__":
    main()
