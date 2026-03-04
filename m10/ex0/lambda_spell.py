def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sort_list = sorted(artifacts, key=lambda x: x['power'], reverse=True)
    return sort_list


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    sort_list = list(filter(lambda x: x['power'] >= min_power, mages))
    return sort_list


def spell_transformer(spells: list[str]) -> list[str]:
    transformed = list(map(lambda x: f"* {x} *", spells))
    return transformed


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    sum_power = sum(map(lambda x: x['power'], mages))
    avg_power = sum_power / len(mages)
    return {"max_power": max_power,
            "min_power": min_power,
            "avg_power": avg_power}


def main():

    artifacts = [
        {
            "name": "Narsil",
            "power": 99,
            "type": "Fire"
        },
        {
            "name": "Master Sword",
            "power": 100,
            "type": "Light"
        }
        ]
    spell_list = ["Avadacadabra",
                  "Ambar aire anar nulla urwa wilma kelva tulka",
                  "lusta arda tanya wista helke neen kuru varya"
                  ]
    mage_list = [
        {
            "name": "Gandalf",
            "power": 300,
        },
        {
            "name": "Frieren",
            "power": 1000,
        },
        {
            "name": "Saruman",
            "power": 299,
        }
        ]

    sorted_artifacts = artifact_sorter(artifacts)
    print("\nTesting artifact sorter...")
    print(
        f"{sorted_artifacts[0]['name']} {(sorted_artifacts[0]['power'])}"
        " comes before "
        f"{sorted_artifacts[1]['name']} {(sorted_artifacts[1]['power'])}"
        )

    print("\nTesting spell transformer...")
    transformed_spell = spell_transformer(spell_list)
    for spell in transformed_spell:
        print(spell, end=" ")
    print("")

    print("\nTesting mage filter...")
    filtered_mages = power_filter(mage_list, 500)
    for mage in filtered_mages:
        print(mage["name"], end=" ")
    print("")

    print("\nTesting mage stats...")
    power_mages = mage_stats(mage_list)
    print(
        f"Max power: {power_mages['max_power']}"
        f" Min power: {power_mages['min_power']}"
        f" Min power: {power_mages['avg_power']}"
          )


if __name__ == "__main__":
    main()
