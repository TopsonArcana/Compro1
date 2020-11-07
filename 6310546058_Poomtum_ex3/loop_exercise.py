def fib(n):
    """This function prints a Fibonacci sequence up to the nth Fibonacci
    """
    a = 0
    b = 1
    for i in range(0, n+1):
        print(b, end="  ")
        a, b = b, a+b
# fill me in


print("fib(n) result:")
n = 0
while n < 10:
    fib(n)
    print("")
    n += 1


def diamond(n):
    """This function prints a diamond shape of size n as shown in loop_exercise_result.txt
    """
    for i in range(n):  # loop expanding pattern
        print(" "*(n-1-i), "*"*(i*2+2))
    for i in range(n-1, -1, -1):  # loop decreasing pattern
        print(" "*(n-1-i), "*"*(i*2+2))


# fill me in

print("diamond(n) result:")
for i in range(0, 8):
    diamond(i)
    print("")


def hailstone(n):
    """This function prints a hailstone sequence whose details can be found in this link:
        http://mathworld.wolfram.com/CollatzProblem.html
    """
    thislist = []
    thislist.append(int(n))
    while n > 1:
        if (n % 2) == 0:
            i = n / 2
            thislist.append(i)
        else:
            i = (3 * n) + 1
            thislist.append(i)
        n = i
    for i in thislist:
        print(int(i), end="  ")
# fill me in


print("hailstone(n) result:")
for i in range(1, 8):
    hailstone(i)
    print("")


def arith_sum(n):
    """This function prints the arithmetic sequence starting from 1 to nth together with its sum
    """
    x = n
    for num in range(n):
        n += num
    for i in range(1, x+1):
        if i != x:
            print(i, end=" + ")
        else:
            x = n
            print(i, x, sep =" = ")
# fill me in


print("arith_sum(n) result:")
for i in range(1, 10):
    arith_sum(i)
