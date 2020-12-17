from item import *
from order import *
from stock import *
from customer import *

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

item1 = Item(1,'T-shirt', 'White')
item2 = Item(2,'T-shirt', 'Black')
item3 = Item(3,'Polo-shirt', 'White')
item4 = Item(4,'Polo-shirt', 'Green')
item5 = Item(5,'Shirt', 'Green')
item6 = Item(6,'Shirt', 'Black')

stock1 = Stock(item1, 100, 60)
stock2 = Stock(item2, 100, 90)
stock3 = Stock(item3, 100, 120)
stock4 = Stock(item4, 100, 140)
stock5 = Stock(item5, 100, 200)
stock6 = Stock(item6, 100, 220)

stock_list = [stock1,stock2,stock3,stock4,stock5,stock6]
print_stock_list(stock_list)

item_list = [item1,item2,item3,item4,item5,item6]
print_item_list(item_list)


## Add your own code to create a list of customers
## Hint: For each customer, you need to read two things from user: 1) name and 2) order_list
## After reading information of each customer, create and print this customer, append each customer to a list of customers
customer_list = []
i = 1
while True:
    print(f"Customer #{i}")
    name = input("Enter name of customer: ")
    order_list = []
    while True:
        id = int(input("Enter item id (negative to quit): "))
        if id < 0:
            break
        amount = int(input("Enter amount: "))
        order_list.append(Order(item_list[id - 1], amount))
    print(Customer(name,order_list))
    customer_list.append(Customer(name,order_list))
    i += 1
    cont = input("Continue to read new customer (y/n): ")
    if cont == "n":
        break



## In the list of customers, process order list of each customer
## After processing order list of all customers, print information of each customer
for customer in customer_list:
    customer.compute_total_cost()
print("\n".join([str(i) for i in customer_list]))
print_stock_list(stock_list)





