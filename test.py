class Vehicle:
     def __init__(self, brand, year):
         self.brand = brand
         self.year = year

     def drive(self):
         print("The vehicle is in motion.")

     def stop(self):
         print("The vehicle has stopped.")


class Car(Vehicle):
     def __init__(self, brand, year, fuel_type):
         super().__init__(brand, year)
         self.fuel_type = fuel_type

def drive(self):
         super().drive()
         print("The car is driving on the road.")


class Bicycle(Vehicle):      
    def __init__(self, brand, year, color):
         super().__init__(brand, year)
         self.color = color

def drive(self):
         print("The bicycle is being pedaled.")


car = Car("Bmw", 2024, "Electric")
car.drive()
car.stop()
print(car.brand)
print(car.year)
print(car.fuel_type)

bicycle = Bicycle("Bastion", 2021, "Black")
bicycle.drive()
bicycle.stop()
print(bicycle.brand)
print(bicycle.year)
print(bicycle.color)
