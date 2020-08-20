import math;

from collections import deque

print('*'*5)

hello="""
maroc
world
"""

print(hello)

x,y=1,2

z:float=5.5

print(x,y)

print(type(x))

print(id(x))

x+=1

print(id(x))

h:str="maazaz"
print(len(h))

print(h[-1])

print(h[:])


first=" zakaria"
last="maazaz"

full= F"{first} {last}"
print(full)

print(full.upper())

print(full.title())

print(full.strip())

print(full.find("maa"))

slug:str=full.replace(" ","-")

print(slug)

print("maroc" not in slug)

a=0b11
b=0x12A

print(b)
print(hex(b))

print(a)
print(bin(a))

# j imaginaire
z=2+5j
print(z)

# quotion
j=5//2
print(j)

# pow
f=5**2
print(f)


PI=3.14
PI=-4

print(PI)

print(round(PI))
print(abs(PI))

print(math.floor(PI))


message="zakaria"
print("ok") if message=="zakaria" else print("not ok")


for x in "maazaz":
    print(x)

    
for x in ['a','b','c']:
    print(x)

for x in range(1,10,2):
    print(x)

guess=0
number=5
#
#while guess!=number:
 #   guess=int(input("Guess: "))

def paire(x:int):
    if x%2==0:
        print("paire")
    else:
        print("impaire")

paire(5)


def function(x,y)-> tuple:
    return (x,x+y)

print(function(1,2)) 

def multiple(*list):
    s=1
    for x in list:
        s=s*x
    return s

print(multiple(1,2,3,4,5))


def usr(**list):
    return list

print(usr(id=1,name='maazaz'))

message="zal"

def fct():
    global message
    if False:
        message="goog"
    print(message)

fct()

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(1, 2, 3))
print("finish")


def fizz_buzz(input):
    if input%3==0 and input%5==0:
        return "fizzbuzz"
    elif input%5==0:
        return "buzz"
    elif input%3==0:
        return "fizz"
    else:
        return input

print(fizz_buzz(7))

f=list(range(10))
h=list("maazaz")
k=h+f
print(k)

t=f[::-2]
print(t)

number=[1,2,3,4,5,6,7,8,9]
first, second, *other= number
print(other)


first,*k,last=number
print(last)

for index,x in enumerate(number):
    print(index,x)

print("/////")
print(number.index(8),number.count(1))

number2=[1,25,90,2,50]
i=sorted(number2,reverse=True)
print(i)

hi=[
    ('maa',1),
    ("aaa",0),
    ("ccc",2),
    ]

def sort_item(item):
    return item[1]

hi.sort(key=lambda item:item[1], reverse=True)
print(hi)

#copie
tt=list(map(lambda item:item[1], hi))

for x in tt:
    print(x)

print(tt)

###############

ss=list(filter(lambda item:item[1]>1, hi))

for x in ss:
    print(x)


#########""

lis=[
    ('maa',1),
    ("aaa",0),
    ("ccc",2),
    ]

x=[y for y in lis if y[1]>=1]
print(x)

##########

x=[1,2,3]
y=[10,20,30]
z="abc"

print(list(zip(x,y,z)))

#################
# lifo
arr=[]
arr.append(1)
arr.append(2)
arr.append(3)
arr.pop()
print(arr)

#fifo
queue= deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

############"



