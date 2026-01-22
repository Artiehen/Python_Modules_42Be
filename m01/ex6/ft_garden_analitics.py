class GardenManager:
    def __init__(self, name):
        self.name = name
        self.orchard = []
        self.stats = self.GardenStats(self.orchard)

    def add_garden(self, orchard):
        self.orchard.append(orchard)

    def grow_all_plants(self):
        for huerto in self.orchard:
            huerto.grow_plants()

    @classmethod
    def create_garden_network(cls, name, list_huertos):
        manager = cls(name)
        for huerto in list_huertos:
            manager.add_garden(huerto)
        return manager

    @staticmethod
    def validate_height(height):
        return height > 0

    class GardenStats:
        def __init__(self, orchard):
            self.orchard = orchard

        def count_plants(self):
            count = 0
            for orchard in self.orchard:
                for plant in orchard.plants:
                    count += 1
            return count

        def total_growth(self):
            total = 0
            for orchard in self.orchard:
                for plant in orchard.plants:
                    total += plant.height
            return total

        def plant_types(self):
            count = {Plant: 0, FloweringPlant: 0, PrizeFlower: 0}
            for orchard in self.orchard:
                for plant in orchard.plants:
                    if isinstance(plant, PrizeFlower):
                        count[PrizeFlower] += 1
                    elif isinstance(plant, FloweringPlant):
                        count[FloweringPlant] += 1
                    else:
                        count[Plant] += 1
            return count

        def garden_score(self):
            score = {Plant: 0, FloweringPlant: 0, PrizeFlower: 0}
            for orchard in self.orchard:
                for plant in orchard.plants:
                    if isinstance(plant, PrizeFlower):
                        score[PrizeFlower] += plant.prize_points + 1
                    elif isinstance(plant, FloweringPlant):
                        score[FloweringPlant] += 1
                    else:
                        score[Plant] += 1
            return score


class Orchard:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        (self.plants).append(plant)

    def grow_plants(self):
        for plant in self.plants:
            plant.grow()

    def calculate_stats(self):
        stats = GardenManager.GardenStats([self])
        return {
            "total_plants": stats.count_plants(),
            "total_growth": stats.total_growth(),
            "plant_types": stats.plant_types(),
            "score": stats.garden_score(),
        }


class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        if not GardenManager.validate_height(self.height):
            self.height = 1
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name, height, color, floracion):
        super().__init__(name, height)
        self.color = color
        self.floracion = floracion
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True
        print(f"{self.name} está floreciendo")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, floracion, prize_points):
        super().__init__(name, height, color, floracion)
        self.prize_points = prize_points

    def award_point(self):
        self.prize_points += 1


def main():
    print("=== Garden Management System Demo ===")
    print("")
    alice_garden = Orchard("Alice")
    bob_garden = Orchard("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", "spring")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", "summer", 10)

    alice_garden.add_plant(oak)
    print("Added Oak Tree to Alice's garden")
    alice_garden.add_plant(rose)
    print("Added Rose to Alice's garden")
    alice_garden.add_plant(sunflower)
    print("Added Sunflower to Alice's garden")

    print("")
    print("Alice is helping all plants grow...")
    alice_garden.grow_plants()
    for plant in alice_garden.plants:
        print(f"{plant.name} grew 1cm")

    manager = GardenManager.create_garden_network(
        "Main Manager", [alice_garden, bob_garden]
    )
    stats = alice_garden.calculate_stats()
    print("")

    print(f"=== {alice_garden.name}'s Garden Report ===")
    print("Plants in garden:")
    for plant in alice_garden.plants:
        desc = f"- {plant.name}: {plant.height}cm"
        if isinstance(plant, FloweringPlant):
            desc += f", {plant.color} flowers"
            if isinstance(plant, PrizeFlower):
                desc += f", Prize points: {plant.prize_points}"
            if plant.is_blooming:
                desc += " (blooming)"
        print(desc)
    print("")

    print(
        f"Plants added: {stats['total_plants']}, Total growth: {stats['total_growth']}cm"
    )
    pt = stats["plant_types"]
    print(
        f"Plant types: {pt[Plant]} regular, {pt[FloweringPlant]} flowering, {pt[PrizeFlower]} prize flowers"
    )
    print("")

    print(f"Height validation test: {GardenManager.validate_height(rose.height)}")

    scores = manager.stats.garden_score()
    print(
        f"Garden scores - Alice: {scores[Plant] + scores[FloweringPlant] + scores[PrizeFlower]}, Bob: 0"
    )

    print(f"Total gardens managed: {len(manager.orchard)}")


if __name__ == "__main__":
    main()