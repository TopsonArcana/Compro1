from item import *
from order import *
from stock import *


def print_stock_list(stocks):
    print("Stock List:")
    print("\n".join([str(i) for i in stocks]))


def print_item_list(items):
    print("Item List: ")
    print("\n".join([str(i) for i in items]))


def print_order_list(orders):
    print("Order List: ")
    print("\n".join([str(i) for i in orders]))


def process_order_list(orders,stocks):
    for order in orders:
        for stock in stocks:
            if order.item == stock.item:
                if order.amount <= stock.amount:
                    stock.amount -= order.amount
                    order.cost = order.amount * stock.price
                    order.status = "Delivered"
                elif order.amount > stock.amount:
                    order.status = "Insufficient"

item1 = Item(1, 'T-shirt', 'White')
item2 = Item(2, 'T-shirt', 'Black')
item3 = Item(3, 'Polo-shirt', 'White')
item4 = Item(4, 'Polo-shirt', 'Green')
item5 = Item(5, 'Shirt', 'Green')
item6 = Item(6, 'Shirt', 'Black')
print(item1)
print(item2)

print(item1 == item2)
print(item2 == item2)

stock1 = Stock(item1, 100, 60)
stock2 = Stock(item2, 100, 90)
stock3 = Stock(item3, 100, 120)
stock4 = Stock(item4, 100, 140)
stock5 = Stock(item5, 100, 200)
stock6 = Stock(item6, 100, 220)
print(stock3)
print(stock5)

order1 = Order(item1, 10)
print(order1)

item_list = [item1,item2,item3,item4,item5,item6]
print_item_list(item_list)

stock_list = [stock1,stock2,stock3,stock4,stock5,stock6]
print_stock_list(stock_list)

order_list = []
while True:
    id = int(input("Enter item id (negative to quit): "))
    if id < 0:
        break
    amount = int(input("Enter amount: "))
    order_list.append(Order(item_list[id-1],amount))
print_order_list(order_list)

process_order_list(order_list, stock_list)

print_order_list(order_list)

print_stock_list(stock_list)
