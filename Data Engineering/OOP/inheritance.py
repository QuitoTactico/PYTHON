class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year) # trae la definición del método de la clase padre, copypaste
        self.battery_capacity = battery_capacity
    
    def display_info(self):   # @OVERRIDE!!!!!
        return f"{self.year} {self.make} {self.model} with {self.battery_capacity} kWh battery"
    


car1 = Car("Mazda", "Miata", 2009)
print(car1.display_info())

car2 = ElectricCar("Mazda", "Miata", 2009, 40)
print(car2.display_info())