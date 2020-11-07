#Problem 1
FEET_IN_MILE = 5280
miles = 13
feet = FEET_IN_MILE * miles
print(feet) 

#Problem 2
hours = 7
minutes = 21
seconds = 37
totalseconds = hours * 3600 + minutes * 60 + seconds
print(totalseconds)

#Problem 3
width = 4
height = 7
perimeter_rec = (2 * width) + (2 * height)
print(perimeter_rec)

#Problem 4
PI = 3.14
radius = 8
area = PI * (radius**2)
print(area)

#Problem 5
present_value = 1000
annual_rate = 7
years = 10
future_value = present_value*((1+0.01*annual_rate)**years)
print(future_value)

#Problem 6
x0,y0 = 2,2
x1,y1 = 5,6
distance = ((x0-x1)**2 +(y0-y1)**2)**0.5
print(distance)

#Problem 7
x0,y0 = 1,1
x1,y1 = 4,1
x2,y2 = 4,5
a = ((x0-x1)**2 +(y0-y1)**2)**0.5
b = ((x1-x2)**2 +(y1-y2)**2)**0.5
c = ((x0-x2)**2 +(y0-y2)**2)**0.5
s = 0.5*(a+b+c)
area = ((s*(s-a)*(s-b)*(s-c)))**0.5
print(area)

#Problem 8
coffee_cup = int(input("Amount of coffee (in cup(s)): "))
water = 200 * coffee_cup
milk = 50 * coffee_cup
coffeebeans = 15 * coffee_cup
print(f"For {coffee_cup} cups of coffee you will need: \n{water} ml of water \n{milk} ml of milk \n{coffeebeans} g of coffee beans")
