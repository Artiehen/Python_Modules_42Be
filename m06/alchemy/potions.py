from .elements import create_fire, create_water, create_earth, create_air


def healing_potion():
    fire = create_fire()
    water = create_water()
    return f"Healing potion brewed with {fire} and {water}"


def strenght_potion():
    fire = create_fire()
    earth = create_earth()
    return f"Healing potion brewed with {earth} and {fire}"


def invisibility_potion():
    air = create_air()
    water = create_water()
    return f"Healing potion brewed with {air} and {water}"


def wisdom_potion():
    fire = create_fire()
    water = create_water()
    earth = create_earth()
    air = create_air()
    return f"Healing potion brewed with {fire} {water} {earth} {air}"
