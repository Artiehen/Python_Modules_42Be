class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0
    
    def get_height(self):
        return(self.__height)
    
    def get_age(self):
        return(self.__age)
    
    def set_height(self, height):
        if height > 0:
            self.__height = height
            print(f"Height Update: {self.get_height()}cm [OK]")
        else:
            print(f"Invalid operation attempt: height {height}cm [REJECTED]")
            print(f"Security: Negative height rejected")
    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f"Age update: {self.get_age()} days [OK]")
        else:
            print(f"Invalid operation attempt: {age} days [REJECTED]")
            print(f"Security: Negative days rejected\n")
            
def main():
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose")
    print(f"Plant Created: {plant.name}")
    plant.set_height(50)
    plant.set_age(-50)
    print(f"Plant Created: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    main()
