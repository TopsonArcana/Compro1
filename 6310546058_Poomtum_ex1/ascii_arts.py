""" Day3 Exercise """

"""
    (if-else)
    Write a Python program to get an integer then,
    print its type. (Hint) use 'mod'

    Example:
        >>> Please enter integer: 40
        40 is even.
        >>> Please enter integer: 29
        29 is odd.
        >>> Please enter integer: 18
        18 is even.
"""

# TODO
integer = int(input('Please enter integer: '))
if (integer % 2) == 0:
    print(f"{integer} is even.")
else:
    print(f"{integer} is odd.")

"""
    (mix)
    Write a Python program to get a list of numbers and,
    count the number of even and odd numbers. 
    (Hint) use 'split()' and casting str to int

    Example:
        >>> Numbers: 1 2 3 4 5 6 7 8 9
        Number of even numbers: 4
        Number of odd numbers: 5

        >>> Numbers: 1 3 5 7 9 
        Number of even numbers: 0
        Number of odd numbers: 5
"""

# TODO
a = [int(x) for x in input('Numbers: ').split()]
even , odd = 0,0
for number in a:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")






"""
    (loop)
    Write a Python program to construct the following pattern, 
    using a nested for loop.

    Expected Output:
        * 
        * * 
        * * * 
        * * * * 
        * * * * * 
"""

# TODO
for row in range(0,5):
    for column in range(0,row + 1):
        print("*", end=" ")
    print("\r")

    
"""
    (loop)
    Write a Python program to get the Fibonacci series between 0 to 50.
    Note : 
        The Fibonacci Sequence is the series of numbers :
            0, 1, 1, 2, 3, 5, 8, 13, 21, ....
    Every next number is found by adding up the two numbers before it.

    Expected Output:
        1 1 2 3 5 8 13 21 34
"""

# TODO
a = 0
b = 1
print("Expected Output:")
while b<50:
    print(b,end=" ")
    a,b = b,a + b

"""
    (if-else)
    Write a Python program to check a triangle is equilateral, isosceles or scalene.
    Note :
        An equilateral triangle is a triangle in which all three sides are equal.
        A scalene triangle is a triangle that has three unequal sides.
        An isosceles triangle is a triangle with (at least) two equal sides.
    (!) Make it simple, no need to care about non-triangle type

    Example:
        >>> Input lengths of the triangle sides:                     
        >>> x: 6                                                                    
        >>> y: 8                                                                    
        >>> z: 12                                                                   
        Scalene triangle 
"""

# TODO
print("\nInput lengths of the triangle sides:")
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
if x == y == z:
    print('Equilateral triangle')
elif x != y != z:
    print('Scalene triangle')
else:
    print('Isosceles triangle')    

"""
    (function)
    Write a function called 'triangle' that get parameter of three sides (x, y, z),
    and 'return' the type of that triangle (from previous problem).

        Example:
        >>> triangle(6, 8, 12)                                                                                                  
        Scalene triangle
"""

# TODO
def triangle(x,y,z):
    if x == y == z:
        return 'Equilateral triangle'
    elif x != y != z:
        return 'Scalene triangle'
    else:
        return 'Isoceles triangle'
print(triangle(6, 8, 12))