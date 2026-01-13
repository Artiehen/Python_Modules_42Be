# =========================
# Plant Family Tree
# =========================

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, bloom_season):
        super().__init__(name, height)
        self.bloom_season = bloom_season


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, bloom_season, award_level):
        super().__init__(name, height, bloom_season)
        self.award_level = award_level


# =========================
# Garden
# =========================

class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def get_statistics(self):
        avg_height = GardenManager.GardenStats.average_height(self.plants)
        tallest = GardenManager.GardenStats.tallest_plant(self.plants)

        return {
            "average_height": avg_height,
            "tallest_plant": tallest.name if tallest else None
        }


# =========================
# Garden Manager + Nested Helper
# =========================

class GardenManager:
    gardens = []

    def add_garden(self, garden):
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        return {
            "total_gardens": len(cls.gardens),
            "garden_names": [garden.name for garden in cls.gardens]
        }

    @staticmethod
    def validate_plant_height(height):
        return height > 0

    # -------- Nested Helper --------
    class GardenStats:

        @staticmethod
        def average_height(plants):
            if not plants:
                return 0

            total_height = 0
            index = 0

            while index < len(plants):
                total_height += plants[index].height
                index += 1

            return total_height / len(plants)

        @staticmethod
        def tallest_plant(plants):
            if not plants:
                return None

            tallest = plants[0]
            index = 1

            while index < len(plants):
                if plants[index].height > tallest.height:
                    tallest = plants[index]
                index += 1

            return tallest

# =========================
# Example Usage
# =========================

print("=== Garden Management System Demo ===\n")

manager = GardenManager()

# Gardens
alice_garden = Garden("Alice's Garden")
joel_garden = Garden("Joel's Garden")

gardens = [joel_garden, alice_garden]

# Plants
oak = FloweringPlant("Oak", 70, "Spring")
tulip = FloweringPlant("Tulip", 25, "Spring")
orchid = PrizeFlower("Orchid", 45, "Summer", "Gold")

plants = [oak, tulip, orchid]

numplants = len(plants)

# Add plants to gardens
alice_garden.add_plant(oak)
alice_garden.add_plant(tulip)
alice_garden.add_plant(orchid)

print(f"Added {oak.name} to {alice_garden.name}")
print(f"Added {tulip.name} to {alice_garden.name}")
print(f"Added {orchid.name} to {alice_garden.name}")

# Register gardens
manager.add_garden(alice_garden)
manager.add_garden(joel_garden)

numgard = len(gardens)

# =========================
# Output
# =========================

print(alice_garden.get_statistics())
print(joel_garden.get_statistics())
print(GardenManager.create_garden_network())
