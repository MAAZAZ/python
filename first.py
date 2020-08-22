import math;
from collections import deque, namedtuple
from array import array
from sys import getsizeof
from pprint import pprint
from timeit import timeit

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

#typle
x=1,2
y=(2,2)
z=x+y
print(type(x))
print(z)

ttt=tuple("hello world")
print(ttt)

############
#swapping
x,y=1,2
x,y=y,x
print(x,y)

########

f=array("i",[1,2,3,4])
f.append(5)
print(f[-1])

#######

kkk=set(number)
hk=1
kkk.add(hk)
jj={10,5}
print(kkk| jj)
print(kkk & jj)
print(kkk - jj)
print(kkk ^ jj)

print(list(kkk)[0])

###########
#dictionary

dic={1:(1,1),"b":(1,2)}
print(list(dic["b"]))

d=dict(a=1,b=2)
print(d.get("a5",0))

del d["a"]
print(d)

d["c"]=50

print(d)
# items() # values() # keys()
for key,x in d.items():
    print(key,x)

##########

# dict comprehension
listt=[x*2 for x in range(5)]
print(listt)

## expr generator
listt=((x,x*2) for x in range(1000))
print(listt)
#for x in listt:
 #   print(x)

print(getsizeof(listt))

listt2=[(x,x*2) for x in range(1000)]
print(getsizeof(listt2))

##############

num=[1,2,3,4,5,6,7,8,9]
print(*num)

## équivalent
num2=list(range(5))
num3=[*range(5), *"hello"]
print(num3)
#########
first=[1]
second=[2,3]

third=[*first,*second] ## third=first+second
print(third)

dic1={"a":1}
dic2=dict(b=2, c=3)
dic3={**dic1,**dic2}
print(dic1.items())
print(dic3.items())

##########"

sentenceOr="This is a common interview question"

def countable(sentence):
    dic={}
    for i in sentence:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    ##del dic[" "] ## eviter les espaces
    #pprint(dic,width=1)
    list=sorted(dic.items(),key=lambda item:item[1],reverse=True)
    #print(list)
    return list[0][0]
    #other solution
    #for i,j in dic.items():
     #   if j==max(dic.values()):
      #      return i

print(countable(sentenceOr))
###########################
## exceptions

number=[1,2,3]
try:
    print("start")
    with open("first.py") as file:
        print("open file")
   # print(number[3])
    x=10/0
except (ValueError,ZeroDivisionError) as err:
    print("problem")
else:
    print("finish")
finally:
    print("ok")
################
code1="""
def divise(num):
    if num==0:
        raise Exception("must not equal 0")
    return 10/num

try:
    print(divise(0))
except Exception as x:
    print(x)
"""

code2="""
def divise(num):
    if num==0:
       return None
    return 10/num

x=divise(0)
if x==None:
    pass
"""
#print("firstcode:", timeit(code1, number=1000))
#print("secondcode:",timeit( code2, number=1000))

## taking twice before using Handler error (raise) because it takes a lot of time

###################"

class Point:
    i="test"
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f'({self.x},{self.y})'

    @classmethod
    def zero(cls):
        return Point(0,0)

    def draw(self):
        print(f"({self.x},{self.y})")
    
    def __eq__(self, value):
        return self.x==value.x and self.y==self.y

    def __add__(self,value):
        p=self.zero()
        p.x=self.x+value.x
        p.y=self.y+value.y
        return p
    
point= Point(1,2)
point.draw()

#print(isinstance(point, Point))

#s:int=15
#s="maazaz"
#print(s)

t=Point.i
t=point.i
#print(t)
#STATIC
Point.i="zakaria"
#not static
point.i="maazaz"
print(Point.i)
print(point.i)

p=Point.zero()
point=Point.zero()
p.draw()

print(str(p))

print(p==point)
p.x=2

k=p+point
k.draw()

#################

class Tag:
    def __init__(self):
        self.__dic=dict()

    @property
    def dic(self):
        return self.__dic
    
    @dic.setter
    def dic(self):
        return self.__dic

    def __getitem__(self,val):
        return self.__dic.get(val.lower(),0)

    def __setitem__(self,val,val2):
        self.__dic[val.lower()]=val2

    #dic=property(getDic,setDic)

tag=Tag()
tag["python"]=1
tag["python"]=2
print(tag["pythons"])
print(tag.__dict__)
tag._Tag__dic['python']=3
print(tag._Tag__dic['python'])
###############""
print(tag.dic)


class humain:
    def __init__(self):
        self.age=18

    def draw(self):
        print(self.age)

class parent:
    def __init__(self):
        self.ismarried=true

    def draw(self):
        print(self.ismarried)

class solder(humain, parent):
    def __init__(self):
        super().__init__()
        self.damage=50

soldr=solder()
print(soldr.age)
print(soldr.damage)
#print(soldr.ismarried)
soldr.draw()

###################"

from pathlib import Path

print(Path().home())
path=Path("PythonProjet/first.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

#print("time: ",ctime(path.stat().st_ctime))
#print(path.read_bytes())

path2=path.with_name("file.txt")
path2=path.with_suffix(".txt")
print(path2.absolute())

path=Path(r"C:\Users\MAAZAZ\Desktop\PythonProjet")
for x in path.iterdir():
    print(x)

ss=[x for x in path.rglob("*.py")]
print(ss)

#####################""

path =Path() / "first.py"
print(path) 

#############"

import json

dicc=[{'id':1,'name':'maazaz zakaria'},{'id':2, 'name':'dsdfds'}]

w=json.dumps(dicc)
print(w)

Path('client.json').write_text(w)

x=Path('client.json').read_text()

print(type(x))

print(type(json.loads(x)))

#############

