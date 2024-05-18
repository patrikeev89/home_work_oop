from abc import ABC, abstractmethod

# Абстрактный класс Товар
class Product(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @abstractmethod
    def info(self):
        pass

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def __str__(self):
        return f"{self._name} - Цена: {self._price} руб."

# Пример наследника - БутылкаВоды
class WaterBottle(Product):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self._volume = volume

    def info(self):
        return f"{self._name} ({self._volume} мл) - Цена: {self._price} руб."

    def __str__(self):
        return f"{self._name} ({self._volume} мл) - Цена: {self._price} руб."

# Пример наследника - ГорячийНапиток
class HotDrink(Product):
    def __init__(self, name, price, volume, temperature):
        super().__init__(name, price)
        self._volume = volume
        self._temperature = temperature

    def info(self):
        return f"{self._name} ({self._volume} мл, {self._temperature}°C) - Цена: {self._price} руб."

    def __str__(self):
        return f"{self._name} ({self._volume} мл, {self._temperature}°C) - Цена: {self._price} руб."
