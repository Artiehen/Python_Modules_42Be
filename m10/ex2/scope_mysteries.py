from typing import Any


def mage_counter() -> callable:
    count = 0

    def ft_count() -> int:
        nonlocal count
        count += 1
        return count
    return ft_count


def spell_accumulator(initial_power: int) -> callable:
    def add_power(power_added: int) -> int:
        try:
            nonlocal initial_power
            initial_power += power_added
            return initial_power
        except Exception:
            print("Invalid Input")
    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    def add_enchantment(item_type: str) -> str:
        nonlocal enchantment_type
        return f"{enchantment_type} {item_type}"
    return add_enchantment


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    mc = mage_counter()
    for i in range(5):
        c = mc()
    print(c)
    s_acc = spell_accumulator(3)
    print(s_acc(5))

    magical_item = enchantment_factory("Flaming")
    print(magical_item("Sword"))

    vault = memory_vault()
    vault["store"]("Hero", "Link")
    vault["store"]("Weapon", "Master Sword")

    print(vault["recall"]("Hero"))
    print(vault["recall"]("Weapon"))
    print(vault["recall"]("spell"))


if __name__ == "__main__":
    main()
