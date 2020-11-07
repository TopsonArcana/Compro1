from cell import *
from player import *
#1
# c1 = Cell(1,2,True)
# print(c1)
# print(c1.occupy_list)

#4
c1 = Cell(1,2,True)
print(c1)
a = Player('A')
b = Player('B')
print(a)
print(b)
print(c1.get_occupy_list_str()) 
c1.add_occupy_list(a)
print(c1.get_occupy_list_str())
c1.add_occupy_list(b)
print(c1.get_occupy_list_str())
c1.remove_occupy_list(a)
print(c1.get_occupy_list_str())
c1.remove_occupy_list(b)
print(c1.get_occupy_list_str()) 


