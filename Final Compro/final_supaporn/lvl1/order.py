class Order:
    def __init__(self, item, amount):
        self.__item = item
        self.__status = "To process"
        self.__amount = amount
        self.__cost = 0

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, value):
        self.__item = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self,value):
        self.__status = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self,value):
        self.__amount = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self,value):
        self.__cost = value

    def __str__(self):
        return f"({str(self.__item)},{self.__amount},{self.__cost} Baht,{self.__status})"