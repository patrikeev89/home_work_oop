from abc import ABC, abstractmethod
from product import WaterBottle, HotDrink

# Интерфейс ТорговыйАвтомат
class VendingMachine(ABC):
    @abstractmethod
    def get_product(self, name):
        pass

    @abstractmethod
    def get_product(self, name, volume=None):
        pass

    @abstractmethod
    def insert_money(self, amount):
        pass

    @abstractmethod
    def buy_product(self, name, volume=None):
        pass

# Пример реализации конкретного типа ТорговогоАвтомата - ПродающийБутылкиВодыАвтомат
class WaterBottleVendingMachine(VendingMachine):
    def __init__(self, products):
        self._products = products
        self._money = 0

    def get_product(self, name, volume=None):
        for product in self._products:
            if product.get_name() == name and (volume is None or (isinstance(product, WaterBottle) and product._volume == volume)):
                return product
        return None

    def insert_money(self, amount):
        self._money += amount

    def buy_product(self, name, volume=None):
        product = self.get_product(name, volume)
        if product:
            if self._money >= product.get_price():
                self._money -= product.get_price()
                return f"Вы купили {product.info()}"
            else:
                return "Недостаточно средств"
        else:
            return "Товар не найден"

# Пример реализации конкретного типа ТорговогоАвтомата - ПродающийГорячиеНапиткиАвтомат
class HotDrinkVendingMachine(VendingMachine):
    def __init__(self, products):
        self._products = products
        self._money = 0

    def get_product(self, name, volume=None, temperature=None):
        for product in self._products:
            if (product.get_name() == name and 
                (volume is None or (isinstance(product, HotDrink) and product._volume == volume)) and
                (temperature is None or (isinstance(product, HotDrink) and product._temperature == temperature))):
                return product
        return None

    def insert_money(self, amount):
        self._money += amount

    def buy_product(self, name, volume=None, temperature=None):
        product = self.get_product(name, volume, temperature)
        if product:
            if self._money >= product.get_price():
                self._money -= product.get_price()
                return f"Вы купили {product.info()}"
            else:
                return "Недостаточно средств"
        else:
            return "Товар не найден"
