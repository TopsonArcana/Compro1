import math
def mysqrt(a):
    x = 1
    y = (x+a/x) /2
    while (abs(y-x) < 0.0000001) == False:
        x = y
        y = (x+a/x) / 2
    return y

def test_square_root():
    print("a    mysqrt(a)       math.sqrt(a)  diff")
    print("-    ---------       ------------  ----")
    for i in range(1,10):
        sq = round(mysqrt(i),11)
        sq2 = round(math.sqrt(i),11)
        print(f"{i:.1f}  {sq:<15} {sq2:<15} {abs(mysqrt(i)-math.sqrt(i))}")
test_square_root()