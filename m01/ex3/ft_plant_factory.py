class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def ft_print_garden(self):
        print(f"Created: {self.name} {self.height}cm {self.age} days")

plants_created = [("Rose", 50, 20), 
                  ("Mango", 480, 1024), 
                  ("Banana", 220, 275), 
                  ("Aguacate", 480, 1024), 
                  ("Pitaya", 220, 275)]

plants = []

index = 0
while index < len(plants_created):
    name, height, age = plants_created[index]
    plants.append(Plant(name, height, age))
    index += 1

print("=== Plant Factory Output ===")

index = 0
while index < len(plants_created):
    plants[index].ft_print_garden()
    index += 1

# count = 0

# while plants_created:
#     plants_created[count]
#     count += 1

# print(count)
