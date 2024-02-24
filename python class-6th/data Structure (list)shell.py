Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py
l=[1,2,0.5,"A","@",[3,4]]
l.append(56)
l
[1, 2, 0.5, 'A', '@', [3, 4], 56]

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py
l
[1, 2, 0.5, 'A', '@', [3, 4], 56]
l[-1]
56
l[6]
56
l[5]
[3, 4]
l[5][0]
3
l[5][1]
4
id(l)
1521093896960
l.count('a')
0
l.count('A')
1
l.index('A')
3
l.index('a')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l.index('a')
ValueError: 'a' is not in list
l.index('@')
4
l
[1, 2, 0.5, 'A', '@', [3, 4], 56]
l[2]=3
l
[1, 2, 3, 'A', '@', [3, 4], 56]

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py
1
2
0.5
A
@
[3, 4]
56

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py
input the value to search 
= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py
input the value to search a
Traceback (most recent call last):
  File "C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py", line 17, in <module>
    if user in l or search.upper() in l:
NameError: name 'search' is not defined

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py
input the value to search a
this is exist

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py
input the value to search a
this is exist

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py
input the value to search hello
this is exist

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py
input the value to search hell
error

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py
Traceback (most recent call last):
  File "C:/Users/Admin1/Desktop/Sudais Usmani/python class-6th/data Structure (list) file.py", line 34, in <module>
    l=[1,2,0.5,hello,"A","@",[3,4]]
NameError: name 'hello' is not defined. Did you mean: 'help'?
help
Type help() for interactive help, or help(object) for help about object.
object
<class 'object'>

type(l)
<class 'list'>
l*2
[1, 2, 0.5, 'A', '@', [3, 4], 56, 1, 2, 0.5, 'A', '@', [3, 4], 56]
l1=[0,9,8,7,6]
l+l1
[1, 2, 0.5, 'A', '@', [3, 4], 56, 0, 9, 8, 7, 6]
2 in l1
False
6 in l1
True
l1[1:3]=[1,2,3]
l
[1, 2, 0.5, 'A', '@', [3, 4], 56]
l1[1:3]
[1, 2]
l
[1, 2, 0.5, 'A', '@', [3, 4], 56]
l1[1:3]
[1, 2]
l1
[0, 1, 2, 3, 7, 6]

:
    
SyntaxError: incomplete input
for x in l:
    print(l)

    
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
>>> for x in l(100):
...     print(l)
... 
...     
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    for x in l(100):
TypeError: 'list' object is not callable
>>> for x in l:
...     print(l)
... 
...     
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
>>> for x in l1:
...     print(l)
... 
...     
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
[1, 2, 0.5, 'A', '@', [3, 4], 56]
l
[1, 2, 0.5, 'A', '@', [3, 4], 56]
l1
[0, 1, 2, 3, 7, 6]
l1[3:5]=1
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    l1[3:5]=1
TypeError: can only assign an iterable
l1[3:5]=[1]
l1
[0, 1, 2, 1, 6]
l1[3:5:6]=[1]
l1
[0, 1, 2, 1, 6]
l1[3:9]=[1]
l1
[0, 1, 2, 1]
l1=[0, 1, 2, 3, 7, 6]
l1
[0, 1, 2, 3, 7, 6]
