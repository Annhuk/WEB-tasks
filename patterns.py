# Створюючі патерни

# Фабричний метод
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def operation(self):
        product = self.factory_method()
        return f"Created {product.operation()}"

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteProductA:
    def operation(self):
        return "ProductA"

# Одинак (Singleton)
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Структурні патерни

# Адаптер
class Target:
    def request(self):
        return "Target behavior"

class Adaptee:
    def specific_request(self):
        return "Adaptee behavior"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()

# Композит
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        return "Composite contains: " + ", ".join(child.operation() for child in self.children)

# Поведінкові патерни

# Стратегія
class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        return self.strategy.algorithm()

class Strategy(ABC):
    @abstractmethod
    def algorithm(self):
        pass

class ConcreteStrategyA(Strategy):
    def algorithm(self):
        return "Algorithm A"

# Спостерігач
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Observer received: {message}")


if __name__ == "__main__":
    # Фабричний метод
    creator = ConcreteCreatorA()
    print("Factory Method:", creator.operation())

    # Одинак (Singleton)
    singleton1 = Singleton()
    singleton2 = Singleton()
    print("Singleton:", singleton1 is singleton2)

    # Адаптер
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print("Adapter:", adapter.request())

    # Композит
    leaf1 = Leaf()
    leaf2 = Leaf()
    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)
    print("Composite:", composite.operation())

    # Стратегія
    strategy = ConcreteStrategyA()
    context = Context(strategy)
    print("Strategy:", context.execute_strategy())

    # Спостерігач
    subject = Subject()
    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()
    subject.attach(observer1)
    subject.attach(observer2)
    subject.notify("Hello, Observers!")

