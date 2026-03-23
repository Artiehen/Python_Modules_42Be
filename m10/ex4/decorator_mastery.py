import time
import re
from functools import wraps


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        t_time = time.time() - start
        print(f"Spell completed in {t_time:.4f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(self_or_power, *args, **kwargs):
            if isinstance(self_or_power, int):
                power = self_or_power
            else:
                power = next((a for a in args if isinstance(a, int)), None)
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self_or_power, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying..."
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and bool(re.fullmatch(r"[A-Za-z ]+", name))

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


@spell_timer
def fireball(damage: int) -> str:
    time.sleep(0.10)
    return f"Fireball deals {damage} damage!"


@power_validator(min_power=10)
def p_validator(spell_name: str, power: int) -> str:
    return f"Successfully cast {spell_name} with power {power}"


@retry_spell(max_attempts=3)
def unstable_spell(call_count):
    call_count["n"] += 1
    if call_count["n"] < 3:
        raise ValueError("Mana unstable!")
    return "Spell succeeded on attempt 3!"


def main() -> None:
    print("\nTesting spell timer...")
    print(fireball(42))
    # print(p_validator("Windgardum Leviosa", 10))

    print("\nTesting retry Spell...")
    call_count = {"n": 0}
    print(unstable_spell(call_count))

    print("\nTesting Mage Guild Class...")

    names = ["X", "Freiren", "Voldemort"]
    for name in names:
        print(f"  '{name}' -> {MageGuild.validate_mage_name(name)}")

    guild = MageGuild()
    print(guild.cast_spell("Zoltraak", 20))
    print(guild.cast_spell("Expelliarmus", 2))


if __name__ == "__main__":
    main()
