# Number 1

from typing import AsyncGenerator


x = [100,110,120,130,140,150]
y=[]
a=1
for a in x:
    a=a*5
    y.append(a)
    
print (y)

# number 2

def divisible_by_three (n):
    x=range(n)
    for i in x:
        if i %3==0:
            print(i)
        

divisible_by_three(15)

# number 3

def flatten():
 x = [[1,2],[3,4],[5,6]]
 flatlist=[]
    
 for sublist in x:
    for element in sublist:
        flatlist.append(element)
 print(flatlist)
flatten()


# number 4
def smallest ():
    n=[2,7,8,9,12,9,9,0]
    return min(n)

print(smallest())

# number 5


def duplicate ():
  x = ['a','b','a','e','d','b','c','e','f','g','h']
  y=set(x)

  print(y)
   
duplicate()

# number 6

def divisible_by_seven():
    y=range(100,200)
    for i in y:
        if i %7==0:
            print(i)
        else :
            print("not divisible by 7")

divisible_by_seven()

# number 7
students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"},{"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
def greeting(*g):
    for student in students:
        print("Hello {}, you were born in the year {}".format(student['name'],2021-student['age']))

greeting()

























