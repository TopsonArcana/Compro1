m1 = 1
n1 = 1
m2 = 4
n2 = 1
m3 = 4
n3 = 5
a = (((m1 - m2)**2) + ((n1 - n2)**2))**0.5
b = (((m2 - m3)**2) + ((n2 - n3)**2))**0.5
c = (((m3 - m1)**2) + ((n3 - n1)**2))**0.5
s = (a+b+c)/2
area1 = ((s * (s - a )*(s - b)*(s - c)))**0.5
print(area1)