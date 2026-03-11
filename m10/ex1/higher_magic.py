def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined()


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """
    Return a new function that multiplies the base spell’s result
    by the given multiplier.
    """
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    Return a function that only casts the spell if condition returns True.
    If the condition fails, return 'Spell fizzled'.
    """
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    """
    Return a function that casts all spells in order.
    Each spell receives the same arguments.
    Return a list of results.
    """
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


def multiplyer() -> int:
    return 3


def base_spell() -> int:
    return 10


def main() -> None:
    combined = spell_combiner(fire, heal)
    print("Combined spell results: ", end="")
    print(f"{combined[0]} hits Dragon, {combined[1]} dragon")
    multi = power_amplifier(fire(), power_amplifier())
    print(multi)


if __name__ == "__main__":
    main()



# higher_magic.py

# def spell_combiner(spell1: callable, spell2: callable) -> callable:
#     """
#     Return a new function that calls both spells with the same arguments
#     and returns a tuple of their results.
#     """
#     def combined(*args, **kwargs):
#         result1 = spell1(*args, **kwargs)
#         result2 = spell2(*args, **kwargs)
#         return (result1, result2)
#     return combined


# def power_amplifier(base_spell: callable, multiplier: int) -> callable:
#     """
#     Return a new function that multiplies the base spell’s result
#     by the given multiplier.
#     """
#     def amplified(*args, **kwargs):
#         return base_spell(*args, **kwargs) * multiplier
#     return amplified


# def conditional_caster(condition: callable, spell: callable) -> callable:
#     """
#     Return a function that only casts the spell if condition returns True.
#     If the condition fails, return 'Spell fizzled'.
#     """
#     def caster(*args, **kwargs):
#         if condition(*args, **kwargs):
#             return spell(*args, **kwargs)
#         return "Spell fizzled"
#     return caster


# def spell_sequence(spells: list[callable]) -> callable:
#     """
#     Return a function that casts all spells in order.
#     Each spell receives the same arguments.
#     Return a list of results.
#     """
#     def sequence(*args, **kwargs):
#         results = []
#         for spell in spells:
#             results.append(spell(*args, **kwargs))
#         return results
#     return sequence
