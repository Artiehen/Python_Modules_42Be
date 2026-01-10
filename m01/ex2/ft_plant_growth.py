class garden:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def ft_print_garden(self):
        print(f"{self.name}: {self.height}cm {self.age} days old")
        
    def ft_plant_growth(self, other):
        print(f"Growth this week: +{other.height - self.height}cm" )


day1 = garden("Rose", 50, 20)
day2 = garden("Rose", 51, 21)
day3 = garden("Rose", 51, 22)
day4 = garden("Rose", 53, 23)
day5 = garden("Rose", 54, 24)
day6 = garden("Rose", 54, 25)
day7 = garden("Rose", 55, 26)

days = [day1, day2, day3, day4, day5, day6, day7]

l = 7
index = 0
while index < l:
    days[index].ft_print_garden()
    index += 1
garden.ft_plant_growth(day1, day7)
