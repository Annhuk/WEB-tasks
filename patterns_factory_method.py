from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_type(self):
        pass


class Car(Vehicle):
    def get_type(self):
        return "Car: A comfortable vehicle for people to drive from point A to point B."


class Truck(Vehicle):
    def get_type(self):
        return "Truck: A vehicle used for transporting heavy goods."


class Motorcycle(Vehicle):
    def get_type(self):
        return "Motorcycle: A two-wheeled vehicle for fast commuting, good choice to avoid traffic jams:)."


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass


class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()


class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()


class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Motorcycle()


if __name__ == "__main__":
    factories = [CarFactory(), TruckFactory(), MotorcycleFactory()]

    for factory in factories:
        vehicle = factory.create_vehicle()
        print(vehicle.get_type())
