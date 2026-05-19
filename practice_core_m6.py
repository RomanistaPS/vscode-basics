# class Item:
#     def calculate_total_price(self, price, quantity):
#         return price * quantity

# item = Item()
# item.name = 'Test name'
# item.price = 1000
# item.quantity = 90

# print(item.__dict__)

# print(item.calculate_total_price(item.price, item.quantity))

# item2 = Item()
# item2.name = 'Test name2'
# item2.price = 500
# item2.quantity = 45

# print(item2.__dict__)

# print(item2.calculate_total_price(item2.price, item.quantity))

# main.py

class Item:
    pay_rate = 0.8 # Price after sale 20%
    all_class_instance = list()

    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all_class_instance.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = round(self.price * self.pay_rate, 2)

    def info(self):
        return f"Item( name:{self.name}, price:{self.price}, quantity:{self.quantity} )"
    @classmethod
    def all_items_info(cls):
        return [item.info() for item in cls.all_class_instance]

    @classmethod
    def load_data_from_csv(cls):
        with open('items.csv', 'r') as file:
            next(file)
            for line in file:
                name, price, quantity = line.strip().split(',')
                # cls(
                Item(
                    name=name.strip('"'),
                    price=float(price),
                    quantity=int(quantity)
                    )

class Phone(Item):
    def __init__(self, name: str, price: float, broken_phones: int, quantity=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

    def info(self):
        return f"Phone( name:{self.name}, price:{self.price}, " \
               f"quantity:{self.quantity}, broken_phones: {self.broken_phones} )"


phone = Phone("Phone16", 78, 945, 13)

print(phone.info())
phone.apply_discount()
print(phone.info())

item = Item("TestItem", 90000, 3)
print(item.info())
item.apply_discount()
print(item.info())