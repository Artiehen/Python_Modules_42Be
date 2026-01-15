class Plant:
    def __init__(self, name, height, age1):
        self.name = name
        self.height = height
        self.age1 = age1
        self.daily_height = height

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age1} days old "
    
    def grow(self, daily_height):
        self.height += daily_height
    
    def age(self):
        self.age1 += 1

def main():
    print("=== Day 1 ===")
    day1 = Plant("Rose", 50, 20)
    print(f"{day1.name}: {day1.height}cm {day1.age1} days old")
    
    index = 0
    while index < 7:
        day1.age()
        day1.grow(1)
        index += 1

    print("=== Day 7 ===")
    print(day1.get_info())
    growth = day1.height - day1.daily_height
    print(f"Growth this week: +{growth}cm")

if __name__ == "__main__":
    main()
