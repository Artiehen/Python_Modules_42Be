class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color, inbloom):
        super().__init__(name, height, age)
        self.color = color
        self.inbloom = inbloom

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter, shade):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade
                  
class Vegetable(Plant):
    def __init__(self, name, harvest, nutrival, height, age):
        super().__init__(name, height, age)
        self.harvest = harvest
        self.nutrival = nutrival

print("\n=== Garden Plant Type ===\n")

# Flowers
flower1 = Flower("Rose", 30, 2, "Red", "is blooming!")
flower2 = Flower("Tulip", 25, 1, "Yellow", "is not blooming :(")

# Trees
tree1 = Tree("Oak", 500, 50, 80, 78)
tree2 = Tree("Pine", 450, 60, 40, 78)

# Vegetables
veg1 = Vegetable("Carrot", "Spring", "is high in Vitamin A", 20, 1)
veg2 = Vegetable("Lettuce", "Fall", "is rich in Fiber", 15, 1)

print(f"{flower1.name}(Flower): {flower1.height}cm, {flower1.age} days, {flower1.color}")
print(f"{flower1.name} {flower1.inbloom}\n")

print(f"{tree1.name}(Tree): {tree1.height}cm, {tree1.age}, {tree1.trunk_diameter}cm diameter")
print(f"{tree1.name} provides {tree1.shade} square meters of shade\n")

print(f"{veg1.name}(Vegetable): {veg1.height}cm, {veg1.age}, {veg1.harvest}")
print(f"{veg1.name} {veg1.nutrival}\n")

# plants = [rose, tulip, oak, pine, carrot, lettuce]

# index = 0
# while index < len(plants):
        
#         print(f"{plants[index].name}: {plants[index].height}cm, {plants[index].age} days")    
#         index += 1
