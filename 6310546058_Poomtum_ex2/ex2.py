print("# Problem 1")
# Problem 1
spin = input("Spin: ")
charge = input("Charge: ")
if spin == "1/2" and charge == "-1/3":
    print("Strange Quark")
elif spin == "1/2" and charge == "2/3":
    print("Charm Quark")
elif spin == "1/2" and charge == "-1":
    print("Electron Lepton")
elif spin == "1/2" and charge == "0":
    print("Neutrino Lepton")
elif spin == "1" and charge == "0":
    print("Photo Boson")
else:
    pass
print("# Problem 2")
# Problem 2
no_1 = float(input())  
no_2 = float(input())
operation = input()
if operation == "+":    #if-else statement to check what operation user input and compute the value
    print(no_1+no_2)    #to the input operation
elif operation == "-":
    print(no_1-no_2)
elif operation == "/":
    if no_2 == 0:
        print("Division by 0!")
    else:
        print(no_1/no_2)
elif operation == "*":
    print(no_1*no_2)
elif operation == "mod":
    if no_2 == 0:
        print("Division by 0!")
    else:
        print(no_1 % no_2)
elif operation == "pow":
    print(no_1**no_2)
elif operation == "div":
    if no_2 == 0:
        print("Division by 0!")
    else:
        print(no_1//no_2)
print("# Problem 3")
# Problem 3
money = int(input("Your money: "))  #if-else check from the highest value animal if false then proceed 
if money >= 6769:  # Sheep          #with the next animal
    sheep = money//6769
    if sheep == 1:  # Check if they're only 1 animal,if false add "s"
        print(f"{sheep} sheep")
    else:
        print(f"{sheep} sheeps")
elif money >= 3848:  # Cow
    cow = money // 3848
    if cow == 1:    # Check if they're only 1 animal,if false add "s"
        print(f"{cow} cow")
    else:
        print(f"{cow} cows")
elif money >= 1296:  # Pig
    pig = money // 1296
    if pig == 1:  # Check if they're only 1 animal,if false add "s"
        print(f"{pig} pig")
    else:
        print(f"{pig} pigs")
elif money >= 678:  # Goat
    goat = money // 678
    if goat == 1:  # Check if they're only 1 animal,if false add "s"
        print(f"{goat} goat")
    else:
        print(f"{goat} goats")
elif money >= 23:  # Chicken
    chicken = money // 23
    if chicken == 1:  # Check if they're only 1 animal,if false add "s"
        print(f"{chicken} chicken")
    else:
        print(f"{chicken} chickens")
else:
    print(None)
print("# Problem 4")
# Problem 4
ref_point = 10.5  # 10:30
offset = int(input("Offset: "))
if ref_point + (offset) >= 24:
    print("Wednesday")
elif ref_point + (offset) >= 0:
    print("Tuesday")
else:
    print("Monday")
print("# Problem 5")
# Problem 5


def is_even(number):
    if number % 2 == 0 and type(number) == int:
        return True
    else:
        return False


print(is_even(5))
print(is_even(6.5))
print(is_even(8))
print("# Problem 6")
# Problem 6


def is_leap_year(year):
    if ((year % 4) == 0 and (year % 100) != 0) or (year % 400) == 0:
        return True
    else:
        return False


print(is_leap_year(2400))
print(is_leap_year(2304))
print(is_leap_year(1240))

print("# Problem 7")
# Problem 7
def interval_intersect(a, b, c, d):
    if c <= a < b >= d:
        return True
    else:
        return False


print(interval_intersect(4, 5, 2, 3))
print(interval_intersect(2, 4, 35, 55))
print(interval_intersect(3, 6, 12, 32))
print("# Problem 8")
# Problem 8


def print_digits(number):
    if number >= 100 or number < 0:
        print("Error: Input is not a two-digit number.")
    else:
        print(
            f"The tens digits is {number//10} and the ones digits is {number%10}")


print_digits(50)
print_digits(99)
print_digits(100)
print("# Problem 9")
# Problem 9


def smaller_root(a, b, c):
    value = ((b**2)-(4*a*c))**1/2
    if value > 0:
        return value
    elif value == 0:
        return value
    else:
        return "Error: No real solution"


print(smaller_root(1, 2, 3))
print(smaller_root(1, 2, 1))
print(smaller_root(1, 4, 1))
print("# Problem 10")
# Problem 10


def there_is_odd(x, y, z):
    for i in x, y, z:
        if i % 2 != 0:
            print(f"There is an odd number whose value is {i}")
            break
        else:
            pass
    if (x and y and z) % 2 == 0:
        print(f"There is no odd number")


there_is_odd(4, 9, 11)
there_is_odd(3, 5, 7)
there_is_odd(4, 6, 8)
print("# Problem 11")
# Problem 11


def list_all_odds(w, x, y, z):
    for i in w, x, y, z:
        if i % 2 != 0:
            print(f"This value is odd {i} ")
    if (w and x and y and z) % 2 == 0:
        print(f"There is no odd number")


list_all_odds(2, 4, 9, 11)
list_all_odds(1, 3, 5, 7)
list_all_odds(2, 4, 6, 8)
print("# Problem 12")
# Problem 12


def max_of_three(x, y, z):
    list = [x, y, z]
    current = list[0]
    for i in range(0, len(list)):   
        if current < list[i]:       #loop each element to check if it's less than the current element
            current = list[i]       #then set current to that value
    print(f"The max value is {current}")


max_of_three(1, 79, 50)
max_of_three(2, 50, 30)
max_of_three(5000, 120391203, 893089124089)
