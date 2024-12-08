class Store:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Изначально ассортимент пустой

    # Добавление товара в ассортимент.
    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен по цене {price}.")

    # Удаление товара из ассортимента
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    # Получение цены товара
    def get_price(self, item_name):
        return self.items.get(item_name, None)

    # Обновление цены
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    # Вывод информации о магазине
    def __str__(self):
        items_str = "\n".join(f"{item}: {price}" for item, price in self.items.items())
        return f"Магазин '{self.name}'\nАдрес: {self.address}\nАссортимент:\n{items_str if items_str else 'Нет товаров'}"


# Создание объектов класса Store
store1 = Store("Магазин у дома", "ул. Ленина, 10")
store2 = Store("Фермерский уголок", "ул. Советская, 25")
store3 = Store("Продукты24", "ул. Мира, 12")

# Добавляем товары
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store2.add_item("картофель", 0.3)
store2.add_item("морковь", 0.4)
store3.add_item("молоко", 1.2)
store3.add_item("хлеб", 0.9)

# Тестирование методов
print(store1)  # Проверяем ассортимент магазина 1
store1.add_item("груши", 0.6)  # Добавляем новый товар
store1.update_price("яблоки", 0.55)  # Обновляем цену товара
store1.remove_item("бананы")  # Удаляем товар
print(f"Цена на яблоки: {store1.get_price('яблоки')}")  # Запрашиваем цену товара
print(store1)  # Проверяем обновленный ассортимент

# Вывод информации о других магазинах
print(store2)
print(store3)
