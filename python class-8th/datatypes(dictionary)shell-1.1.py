Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/Admin1/Desktop/Sudais Usmani/python class-8th/datatypes(dictionary)file-1.1.py
d
{1: 'PAK', 2: 'AFG', 3: 'GER'}
x=list(d.values())
x
['PAK', 'AFG', 'GER']
y=list(d.key())
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    y=list(d.key())
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
y=list(d.keys())
y
[1, 2, 3]
z=list(d.items())
z
[(1, 'PAK'), (2, 'AFG'), (3, 'GER')]
z[0]
(1, 'PAK')
z[2]
(3, 'GER')
z[1]
(2, 'AFG')
z[0][0]
1
z[0][2]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    z[0][2]
IndexError: tuple index out of range
z[0][1]
'PAK'
d
{1: 'PAK', 2: 'AFG', 3: 'GER'}
d[4]="END"
d
{1: 'PAK', 2: 'AFG', 3: 'GER', 4: 'END'}
d[2]="CAN"
s
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s
NameError: name 's' is not defined
d
{1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END'}
d
{1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END'}
print(d.type)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(d.type)
AttributeError: 'dict' object has no attribute 'type'
d.type
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d.type
AttributeError: 'dict' object has no attribute 'type'
dict.update({'4':'AUS'})
d
{1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END'}
d.update({'4':'AUS'})
d
{1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END', '4': 'AUS'}
d
{1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END', '4': 'AUS'}
d.pop()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
d.pop('4')
'AUS'
d
{1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END'}
d={1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END', '4': 'AUS'}
d
{1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END', '4': 'AUS'}
d.popitem('4')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d.popitem('4')
TypeError: dict.popitem() takes no arguments (1 given)
d.popitem(')
          
SyntaxError: incomplete input
d.popitem()
          
('4', 'AUS')
d={1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END', '4': 'AUS'}
          
del d['4']
          
d
          
{1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END'}
d.clear()
          
d
          
{}
d={1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END', '4': 'AUS'}
          
d_2=d.copy()
          
d_2
...           
{1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END', '4': 'AUS'}
>>> d_2[2]
...           
'CAN'
>>> d_2['2']
...           
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d_2['2']
KeyError: '2'
>>> d_2.pop()
...           
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    d_2.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d_2.popitem()
...           
('4', 'AUS')
>>> d_2
...           
{1: 'PAK', 2: 'CAN', 3: 'GER', 4: 'END'}
