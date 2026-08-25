# OOPs --> Object oriented programming languages

    # Class
    # Object
    # inheritance
    # Polymorphism
    # Encapsulation
    # Abstraction

# Class --> Template

# Members 
    # 1. Data Members
    # 2. Member function

class Car:
    def __init__(self, wheels, sheets, colors, fuel):
        self.no_of_wheels = wheels
        self.no_of_sheets = sheets
        self.color = colors
        self.fuel_type = fuel

    def speed(self):
        print("Car speed")

    def __del__(self):
        print("It's a Destructor")

BMW = Car(4, 7, "Red", "Petrol") 
Audi = Car(5, 5, "Black", "Disel")

print("-----BMW-----")
print(BMW.no_of_wheels)
print(BMW.color)

print("\n-----Audi-----")
print(Audi.no_of_wheels)
print(Audi.color)
