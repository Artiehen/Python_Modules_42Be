class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def ft_print_garden(self):
        print(f"{self.name}: {self.height}cm {self.age} days old")
    
# Create plant objects

plant1= Plant("Rose", 50, 20)
plant2= Plant("Mango", 480, 1024)
plant3= Plant("Banana", 220, 275)

# # Store them in a list
plants = [plant1, plant2, plant3]
print("=== Garden Plant Registry ===")

index = 0
while index < 3:
    plants[index].ft_print_garden()
    index += 1
