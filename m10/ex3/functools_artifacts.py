import functools
from functools import lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation not in ["add", "multiply", "max", "min"]:
        return -1
    else:
        if operation == "add":
            return functools.reduce(lambda a, b: a + b, spells)
        elif operation == "multiply":
            return functools.reduce(lambda a, b: a * b, spells)
        elif operation == "max":
            return functools.reduce(lambda a, b: a if a > b else b, spells)
        elif operation == "min":
            return functools.reduce(lambda a, b: a if a < b else b, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": functools.partial(enchantment,
                                          power=20, element="fire"),
        "ice_enchant": functools.partial(enchantment, power=20, element="ice"),
        "lightning_enchant": functools.partial(enchantment,
                                               power=20, element="lightning")
        }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return "Please input valid positive number!"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @singledispatch
    def cast_spell(arg):
        return f"Unknown spell type: {type(arg).__name__}"

    @cast_spell.register(int)
    def _(damage: int) -> str:
        return f"Damage spell: deals {damage} damage!"

    @cast_spell.register(str)
    def _(enchantment: str) -> str:
        return f"Enchantment spell: {enchantment} applied!"

    @cast_spell.register(list)
    def _(spells: list) -> str:
        results = [cast_spell(spell) for spell in spells]
        return f"Multi-cast: {', '.join(results)}"

    return cast_spell


def enchantment(power: int, element: str, target: str) -> str:
    return f"{target} attacked with {element} dealing {power} damage"


def main() -> None:
    try:
        print("Testing Spell Reducer=================\n")
        spells_power = [4, 5, 2, 1, 7]
        print(spell_reducer(spells_power, "add"))
        print(spell_reducer(spells_power, "multiply"))
        print(spell_reducer(spells_power, "max"))
        print(spell_reducer(spells_power, "min"))

        print("\nTesting Partial Enchanter=========================\n")

        enchant = partial_enchanter(enchantment)
        for en in ["fire_enchant", "ice_enchant", "lightning_enchant"]:
            print(f"{en}: {enchant[f'{en}'](target='Monster')}")

        print("\nTesting Memoized Fibonacci====================\n")

        print(memoized_fibonacci(0))
        print(memoized_fibonacci(1))
        print(memoized_fibonacci(10))
        print(memoized_fibonacci(50))

        print("\nTesting Spell Dispatcher===============================\n")

        cast = spell_dispatcher()

        print(cast(42))
        print(cast("Fireball"))
        print(cast([10, "Frost", 99]))
        print(cast(3.14))
    except Exception:
        print("Invalid Input")


if __name__ == "__main__":
    main()
