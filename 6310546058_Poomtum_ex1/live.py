import sys
def is_triangle(l1,l2,l3):
    if (l1+l2>l3) and (l2+l3>l1) and (l1+l3>l2):
        print("It's a triangle.")
        return True
    else:
        print("It's not a triangle.")
        return False
def read_nonnegative():
    num = (float(input("Enter 1st line's length: ")))
    if num < 0:
        print("Invalid value: input must be nonnegative")
        sys.exit()
    num2 = (float(input("Enter 2nd line's length: ")))
    if num2 < 0:
        print("Invalid value: input must be nonnegative")
        sys.exit()
    num3 = (float(input("Enter 3rd line's length: ")))
    if num3 < 0:
        print("Invalid value: input must be nonnegative")
        sys.exit()
    return num,num2,num3                 
a,b,c = read_nonnegative()
is_triangle(a,b,c)