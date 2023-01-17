from utils import request_analyses


class Storage:
    capacity = 0

    def __init__(self):
        self.items = {}

    def add(self, title, quantity):
        self.items[title] = self.items.get(title, 0) + quantity
        return title, quantity

    def remove(self, title, quantity):
        self.items[title] = self.items.get(title) - quantity
        return self.items[title]

    def get_items(self):
        return dict(self.items)

    def get_free_space(self):
        return self.capacity - self.get_unique_items_count()

    def get_unique_items_count(self):
        return len(self.items)


class Store(Storage):
    capacity = 100

    def __init__(self):
        super().__init__()

    def add(self, title, quantity):
        if self.get_free_space() == 0:
            print("Место на складе закончилось")
            return None, None
        else:
            return super().add(title, quantity)

    def remove(self, title, quantity):
        available = True
        if title in self.items:
            if self.items[title] > quantity:
                self.items[title] = super().remove(title, quantity)
                return available, title, quantity, self.items[title]
            else:
                quantity = self.items[title]
                self.items.pop(title)
                return available, title, quantity, None
        else:
            available = False
            return available, "Unknown", 0, 0


class Shop(Store):
    capacity = 5

    def __init__(self):
        super().__init__()


class Request:

    def __init__(self, from_, to_, product, quantity):
        self.from_ = from_
        self.to_ = to_
        self.product = product
        self.quantity = quantity


def request_execution(from_, to_, product, quantity):
    if from_ == 'store' and to_ == 'shop':
        if shop.get_free_space() > 0:
            (available, product_off, quantity_off, remain_stock_off) = store.remove(product, int(quantity))
            if not available:
                print("Продукта нет на складе")
            else:
                print("Нужное кол-во на складе есть!")
                print(f"Курьер забрал {quantity_off} {product_off} со склада и везет в магазин")
                quantity = quantity_off
                (product_add, quantity_add) = shop.add(product, int(quantity))
                print(f"Курьер доставил {quantity_add} {product_add} в магазин")
        else:
            print("В магазине нет места")

    if from_ == 'shop' and to_ == 'store':
        if store.get_free_space() > 0:
            (available, product_off, quantity_off, remain_stock_off) = shop.remove(product, int(quantity))
            if not available:
                print("Продукта нет в магазине")
            else:
                print(f"Курьер забрал {quantity_off} {product_off} из магазина и везет на склад")
                quantity = quantity_off
                (product_add, quantity_add) = store.add(product, int(quantity))
                print(f"Курьер доставил {quantity_add} {product_add} на склад")
        else:
            print("На складе нет места")
    return "Операция завершена"


store = Store()
store.add("Помидоры", 20)
store.add("Бананы", 50)
store.add("Томаты", 30)
store.add("Икра", 52)

shop = Shop()
shop.add("Кабачки", 10)
shop.add("Помидоры", 3)
shop.add("Томаты", 4)
shop.add("Икра", 2)
shop.add("Печеньки", 6)
shop.add("Макароны", 7)

while True:
    request = input("Запрос пользователя: ")
    if request != 'end':
        (from_, to_, product, quantity) = request_analyses(request)
        requests = Request(from_, to_, product, quantity)
        print(request_execution(requests.from_, requests.to_, requests.product, requests.quantity))
        print("На складе осталось:", end='\n')
        print(store.get_items())
        print("В магазине осталось: ", end='\n')
        print(shop.get_items())
    else:
        break