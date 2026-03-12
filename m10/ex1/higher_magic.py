from typing import List


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence


def fire() -> str:
    return "fireball"


def heal() -> str:
    return "heal"


def base_spell() -> int:
    return 10


def condition() -> bool:
    return False


def fissure() -> str:
    return "Fissure"


def guillotine() -> str:
    return "Guillotine"


def horn_drill() -> str:
    return "Horn Drill"


def sheer_cold() -> str:
    return "Sheer Cold"


def spell_list() -> List[callable]:
    return [fissure, guillotine, horn_drill, sheer_cold]


def main() -> None:
    try:
        print("\nTesting Spell Combiner")
        combined = spell_combiner(fire, heal)
        print("Combined spell results: ", end="")
        print(f"{combined()[0]} hits Dragon, {combined()[1]} dragon")
        print("\nTesting Spell Power Amplifier")
        multi = power_amplifier(base_spell, 2)
        print(f"Original: {base_spell()}, Amplified: {multi()}")
        print("\nTesting Conditional Caster")
        conditional_func = conditional_caster(condition, fire)
        print(f"{conditional_func()}")
        print("\nTesting Spell Sequence")
        spell_seq = spell_sequence(spell_list())
        print(spell_seq())
    except Exception:
        print("Please check functions")


if __name__ == "__main__":
    main()
