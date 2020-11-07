#Action functions
def buy():
    global water_stock,milk_stock,bean_stock,cup_stock,money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:")
    recipe = int(input())
    if recipe == 1:
        water_stock -= 250
        bean_stock -= 16
        cup_stock -= 1
        money += 4
    elif recipe == 2:
        water_stock -= 350
        milk_stock -= 75
        bean_stock -= 20
        cup_stock -= 1
        money += 7
    else:
        water_stock -= 200
        milk_stock -= 100
        bean_stock -= 12
        cup_stock -= 1
        money += 6
    print(f"The coffee machine has: \n{water_stock} ml of water \n{milk_stock} ml of milk \n{bean_stock} g of coffee beans \n{cup_stock} disposable cups\n{money}$ of money ")
def fill():
    global water_stock,milk_stock,bean_stock,cup_stock,money
    print("Write how many ml of water do you want to add:")
    wfill = int(input())
    water_stock += wfill
    print("Write how many ml of milk do you want to add:")
    mfill = int(input())
    milk_stock += mfill
    print("Write how many grams of coffee beans do you want to add:")
    bfill = int(input())
    bean_stock += bfill
    print("Write how many disposable cups of coffee do you want to add:")
    cfill = int(input())
    cup_stock += cfill
    print(f"The coffee machine has: \n{water_stock} ml of water \n{milk_stock} ml of milk \n{bean_stock} g of coffee beans \n{cup_stock} disposable cups\n{money}$ of money ")
def take():
    global money
    print(f"I gave you ${money}")
    money -= money
    print(f"The coffee machine has: \n{water_stock} ml of water \n{milk_stock} ml of milk \n{bean_stock} g of coffee beans \n{cup_stock} disposable cups\n{money}$ of money ")

#Coffee Machine STOCK
water_stock = 400 
milk_stock = 540 
bean_stock = 120
cup_stock = 9
money = 550

#Print Coffee states
print(f"The coffee machine has: \n{water_stock} ml of water \n{milk_stock} ml of milk \n{bean_stock} g of coffee beans \n{cup_stock} disposable cups\n{money}$ of money ")

#Ask action
print("Write action (buy,fill,take):")
action = input()
if action == "buy":
    buy()
elif action == "fill":
    fill()
elif action == "take":
    take()
else:
    pass