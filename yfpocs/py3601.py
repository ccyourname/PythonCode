
#coding=gbk
#数据库连接
import pyodbc
#import pypyodbc
import time
import sys
#链接数据库 常熟正式库
conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
#增加数据库游标 
cursor = conn.cursor()
#读取SQL语句
cursor.execute("select * from mfg_part where partno = 11985184 ")
#row = cursor.fetchone()
rowall = cursor.fetchall()
for re in rowall:
    print(re)
time.sleep(5)

'''def func1(x):
    sum=0
    for i in range(x+1):
        sum+=i
    return sum
print(func1(100))
def func2(x):
    sum=0
    for i in range(x+1):
        sum +=i**2
    return sum
print(func2(4))

def func3(x):
    sum = 2*3.14*x**2
    return sum

print(int(func3(5)))

def abs (x):
    if x >0:
        return x
    elif x<0:
        return -x
print(abs(-10))

l = []
n=1
while n<99:
    l.append(n)
    n +=2
print(l)
print(l[2])
def left(n):
    for a in range (n):
        
        return l[n-1]
'''
'''print(left(3))
print(l[0:3])
print(l[-3:])
aa = list(range(100))
print (aa)
a2 = 'abcdefg'
print(a2[:3])
print(aa[::2])
print(aa[-1:0:2])
a3={'a': 'ddd','b':2,'c':3}
print(a3)
for key in a3:
    print(key)
for value in a3.values():
    print(value)
for k ,v in a3.items():
    print(k,v)
    
for i in enumerate(a2):
    print(i)
a4 = [x*x for x in range(1,11) if x % 3==0]
a5=[m+n for m in 'ABC' for n in 'abcdefg']
print(a5)
import os
a6 = [d for d in os.listdir()]
print(a6)
a7 = [d for d in os.listdir('.')]
print(a7)
a8=['AA','BB',33,'DD']
a9=[m.lower() for m in a8 if isinstance(m,str)]
print(a8)

print(a9)
'''
'''
l1=[list(range(11))]
l2=[x for x in range(11)]
print(l2)
g=(x for x in range(11))
print(g)
for n in g:
    print(n)
'''
'''
def fib(max):
    n,a,b=0,0,1
    while n < max:
        print(b)
        a,b=b,a+b
        n+=1
    return "eng"
'''
'''
def fib2(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n+=1
    return "eng"        
'''
'''
for n in fib2(4):
    print(n)

g1 = fib2(6)
print(g1)

while True :
    try:
        x=next(g1)
        print(x)
    except StopIteration as e:
        print('111',e.value)
        break
'''