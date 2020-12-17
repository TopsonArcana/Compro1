class Stock:
    def __init__(self, item, amount, price):
        self.__item = item
        self.__amount = amount
        self.__price = price

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, value):
        self.__item = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        return f"({str(self.__item)},{self.__amount},{self.__price})"
