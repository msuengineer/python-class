Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> l=[1,2,3]
>>> l1=l.copy()
>>> l1
[1, 2, 3]
>>> l1[2]="a"
>>> l1
[1, 2, 'a']
>>> l
[1, 2, 3]
>>> l2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l2
NameError: name 'l2' is not defined. Did you mean: 'l'?
>>> l2=l1
l2
[1, 2, 'a']
l2,l3=l1
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    l2,l3=l1
ValueError: too many values to unpack (expected 2)
l1=[1,2,3]
l2=l1
l2
[1, 2, 3]
l1=l.copy
l
[1, 2, 3]
l1
<built-in method copy of list object at 0x000001AF97844BC0>
l2
[1, 2, 3]
l
[1, 2, 3]
li
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    li
NameError: name 'li' is not defined. Did you mean: 'l'?
l1
<built-in method copy of list object at 0x000001AF97844BC0>
li=[1,2,3]
12=[1,2,3]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l2=[1,2,3]
l3=[1,2,3]
b=[a,b,c,d,e,f]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b=[a,b,c,d,e,f]
NameError: name 'a' is not defined
b=['a','b','c','d','e','f']
c=b.copy()
c
['a', 'b', 'c', 'd', 'e', 'f']
a=b+c
a
['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f']
a.upper()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
print(a.upper())
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(a.upper())
AttributeError: 'list' object has no attribute 'upper'
a
['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f']
x=[1,2,3,4,5,6,7,8,9,0]
max(x)
9
min(x)
0
len(x)
10
x[0]="2"
x
['2', 2, 3, 4, 5, 6, 7, 8, 9, 0]
x[0]=1
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-7th/typil (file).py
