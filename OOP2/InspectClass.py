class Engine:
    horsepower = 10

class Vehicle(Engine):
    vehicleEngine = Engine.horsepower



#just neet to change wich Class you want to inspect
print(dir(Vehicle))
