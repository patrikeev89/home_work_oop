from product import WaterBottle, HotDrink
from vendingmachine import WaterBottleVendingMachine, HotDrinkVendingMachine

def main():
    water_products = [
        WaterBottle("Вода Evian", 100, 500),
        WaterBottle("Вода BonAqua", 50, 500),
        WaterBottle("Вода Aqua Minerale", 60, 500),
        WaterBottle("Вода Aqua Minerale", 80, 1000)
    ]

    hot_drink_products = [
        HotDrink("Кофе", 150, 300, 90),
        HotDrink("Чай", 100, 250, 85),
        HotDrink("Какао", 120, 200, 80)
    ]

    water_machine = WaterBottleVendingMachine(water_products)
    hot_drink_machine = HotDrinkVendingMachine(hot_drink_products)

    # Тестирование WaterBottleVendingMachine
    print(water_machine.buy_product("Вода Evian"))  # Товар не найден, так как нет денег
    water_machine.insert_money(100)
    print(water_machine.buy_product("Вода Evian"))  # Покупка успешна
    water_machine.insert_money(50)
    print(water_machine.buy_product("Вода BonAqua"))  # Покупка успешна
    print(water_machine.buy_product("Вода Aqua Minerale"))  # Недостаточно средств
    water_machine.insert_money(80)
    print(water_machine.buy_product("Вода Aqua Minerale", 1000))  # Покупка успешна
    product = water_machine.get_product("Вода Aqua Minerale", 1000)
    if product:
        print(f"Найден продукт: {product}")
    else:
        print("Товар не найден")

    # Тестирование HotDrinkVendingMachine
    print(hot_drink_machine.buy_product("Кофе", 300, 90))  # Товар не найден, так как нет денег
    hot_drink_machine.insert_money(150)
    print(hot_drink_machine.buy_product("Кофе", 300, 90))  # Покупка успешна
    hot_drink_machine.insert_money(100)
    print(hot_drink_machine.buy_product("Чай", 250, 85))  # Покупка успешна
    print(hot_drink_machine.buy_product("Какао", 200, 80))  # Недостаточно средств
    hot_drink_machine.insert_money(120)
    print(hot_drink_machine.buy_product("Какао", 200, 80))  # Покупка успешна
    product = hot_drink_machine.get_product("Кофе", 300, 90)
    if product:
        print(f"Найден продукт: {product}")
    else:
        print("Товар не найден")

if __name__ == "__main__":
    main()
