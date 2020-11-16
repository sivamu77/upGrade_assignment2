#1.

ll=[]
for i in range(10):
    x=int(input())
    if x%2==0:
        ll.append(x)
print(ll)
#2.
li1=[1,2,3,4,5]
print(li1)
li2='lets UpGrade'
b=[i for i in li2]
print(b)

#3

value=int(input())
dic_of_val={}
for i in range(1,value):
   dic_of_val[i]=i*i
print(dic_of_val)

# 4
import math
(x,y)=(0,0)
for i in range(int(input())):
    a,b=input().split()
    a,b=str(a),int(b)
    if a=="DOWN":x,y=x,y-b
    elif a=="LEFT":x,y=x-b,y
    elif a=="RIGHT":x,y=x+b,y
    else:x,y=x,y+b
print(round(math.sqrt((x**2)+(y**2))))