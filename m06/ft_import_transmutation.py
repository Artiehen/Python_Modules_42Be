def method_1():
    try:
        import alchemy.elements
        x = "alchemy.elements.create_fire():"
        print("Method 1 - Full module import:")
        print(f"{x} {alchemy.elements.create_fire()}")
    except Exception as e:
        print(e)


def method_2():
    try:
        from alchemy.elements import create_water
        print("\nMethod 2 - Specific function import:")
        print(f"create_water(): {create_water()}")
    except Exception as e:
        print(e)


def method_3():
    try:
        from alchemy.potions import healing_potion as heal
        print("\nMethod 3 - Aliased import:")
        print(f"heal: {heal()}")
    except Exception as e:
        print(e)


def method_4():
    try:
        from alchemy.elements import create_water, create_fire
        from alchemy.potions import strenght_potion
        print("\nMethod 4 - Multiple imports")
        print(f"create_earth(): {create_water()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strenght_potion: {strenght_potion()}")
    except Exception as e:
        print(e)


def transmutation():
    try:
        print("\n=== Import Transmutation Mastery ===")
        method_1()
        method_2()
        method_3()
        method_4()

        print("\nAll import transmutation methods mastered!")
    except Exception as e:
        print(e)


transmutation()
