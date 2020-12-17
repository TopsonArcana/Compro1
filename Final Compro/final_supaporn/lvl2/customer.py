class Customer:
    def __init__(self, name, order_list):
        self.__name = name
        self.__order_list = order_list
        self.__total_cost = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def order_list(self):
        return self.__order_list

    @order_list.setter
    def order_list(self, value):
        self.__order_list = value

    @property
    def total_cost(self):
        return self.__total_cost

    @total_cost.setter
    def total_cost(self, value):
        self.__total_cost = value

    def __str__(self):
        order_str = "\n".join([str(i) for i in self.__order_list])
        return f"Customer: {self.__name}\nTotal cost = {self.__total_cost}\n{order_str}"

    def compute_total_cost(self):
        for i in self.__order_list:
            self.__total_cost += i.cost
