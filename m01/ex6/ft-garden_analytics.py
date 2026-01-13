class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class FloweringPlant(Plant):
    def __init__(self, name, height, season):
        super().__init__(name, height)
        self.season = season

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, season, award_level):
        super().__init__(name, height, season)
        self.award_level = award_level

class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

        def add_plant(self, plant):
            self.plants.append(plant)

        def get_stats(self):
            avg_height = GardenManager.GardenStats.average_height(self.plant)
            tallest = GardenManager.GardenStats.tallest_plant(self.plants)

        return {
            "average_height": avg_height,
            "tallest_plant": tallest.name if tallest else None
        }

class GardenManager:
    gardens = []
    class GardenStats:
        @staticmethod
        def avg_height(plants):
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
        
manager = GardenManager()

# Gardens
rose_garden = Garden("Rose Garden")
exhibition_garden = Garden("Exhibition Garden")

# Plants
rose = FloweringPlant("Rose", 30, "Spring")
tulip = FloweringPlant("Tulip", 25, "Spring")
orchid = PrizeFlower("Orchid", 45, "Summer", "Gold")

# Add plants to gardens
rose_garden.add_plant(rose)
rose_garden.add_plant(tulip)
exhibition_garden.add_plant(orchid)

# Register gardens
manager.add_garden(rose_garden)
manager.add_garden(exhibition_garden)

# =========================
# Output
# =========================

print(rose_garden.get_statistics())
print(exhibition_garden.get_statistics())
print(GardenManager.create_garden_network())