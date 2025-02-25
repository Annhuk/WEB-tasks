from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass


class PhoneApp(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"{self.name} App: New temperature update -> {temperature}°C")


class DesktopApp(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"{self.name} Desktop App: Temperature updated to {temperature}°C")


class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class WeatherStation(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_temperature(self, temperature):
        print(f"\nWeather Station: Temperature changed to {temperature}°C")
        self.temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)


if __name__ == "__main__":

    station = WeatherStation()

    app1 = PhoneApp("SYNOPTYK")
    app2 = PhoneApp("Summer soon")
    desktop = DesktopApp("Meteo Mateo")

    station.add_observer(app1)
    station.add_observer(app2)
    station.add_observer(desktop)

    station.set_temperature(25)
    station.set_temperature(30)

    station.remove_observer(app2)
    station.set_temperature(20)
