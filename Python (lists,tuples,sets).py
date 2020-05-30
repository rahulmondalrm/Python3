Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Lists in Python
>>> x=[1,5,3,4,8,9,2]
>>> x
[1, 5, 3, 4, 8, 9, 2]
>>> x[0]
1
>>> y=['max',2,52.5,[3,2]]
>>> y
['max', 2, 52.5, [3, 2]]
>>> y[3]
[3, 2]
>>> len(x)
7
>>> len(y)
4
>>> x.insert(2,'Tom')
>>> x
[1, 5, 'Tom', 3, 4, 8, 9, 2]
>>> x.remove('Tom')
>>> x
[1, 5, 3, 4, 8, 9, 2]
>>> x.insert(0,1)
>>> x
[1, 1, 5, 3, 4, 8, 9, 2]
>>> x.remove(1)
>>> x
[1, 5, 3, 4, 8, 9, 2]
>>> x.pop()
2
>>> x
[1, 5, 3, 4, 8, 9]
>>> x.pop()
9
>>> x
[1, 5, 3, 4, 8]
>>> z=[1,5,4,9,8,2]
>>> z
[1, 5, 4, 9, 8, 2]
>>> del z
>>> z
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> z=[4,5,2,7,1,3]
>>> z
[4, 5, 2, 7, 1, 3]
>>> z.clear()
>>> z
[]
>>> x
[1, 5, 3, 4, 8]
>>> x.sort()
>>> x
[1, 3, 4, 5, 8]
>>> x.insert(3.'Tom')
SyntaxError: invalid syntax
>>> x.insert(3,'Tom')
>>> x
[1, 3, 4, 'Tom', 5, 8]
>>> x.sort()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> x.delete(tom)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x.delete(tom)
AttributeError: 'list' object has no attribute 'delete'
>>> x.delete(Tom)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    x.delete(Tom)
AttributeError: 'list' object has no attribute 'delete'
>>> x
[1, 3, 4, 'Tom', 5, 8]
>>> x.delete(5)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    x.delete(5)
AttributeError: 'list' object has no attribute 'delete'
>>> x.remove(Tom)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x.remove(Tom)
NameError: name 'Tom' is not defined
>>> x
[1, 3, 4, 'Tom', 5, 8]
>>> x.remove('Tom')
>>> x
[1, 3, 4, 5, 8]
>>> x.sort()
>>> x
[1, 3, 4, 5, 8]
>>> x.reverse()
>>> x
[8, 5, 4, 3, 1]
>>> x.append(10)
>>> x
[8, 5, 4, 3, 1, 10]
>>> s=x.copy()
>>> s
[8, 5, 4, 3, 1, 10]
>>> x.append(10)
>>> x
[8, 5, 4, 3, 1, 10, 10]
>>> x.count(10)
2
>>> x.count(100)
0
>>> 
>>> # Tupple
>>> x=(5,2,4,6,7,9)
>>> x
(5, 2, 4, 6, 7, 9)
>>> x[2]
4
>>> x(5)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    x(5)
TypeError: 'tuple' object is not callable
>>> x[3]
6
>>> x[0]=2
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    x[0]=2
TypeError: 'tuple' object does not support item assignment
>>> x.count(x)
0
>>> x.count(2)
1
>>> len(x)
6
>>> y=(5,'Max',52.5,[3,2])
>>> y
(5, 'Max', 52.5, [3, 2])
>>> y[4]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    y[4]
IndexError: tuple index out of range
>>> y[3]
[3, 2]
>>> x
(5, 2, 4, 6, 7, 9)
>>> y
(5, 'Max', 52.5, [3, 2])
>>> z=x+y
>>> z
(5, 2, 4, 6, 7, 9, 5, 'Max', 52.5, [3, 2])
>>> x.sort()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    x.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> max(x)
9
>>> x
(5, 2, 4, 6, 7, 9)
>>> a=('hifi',) * 5
>>> a
('hifi', 'hifi', 'hifi', 'hifi', 'hifi')
>>> a=('hifi') * 5
>>> a
'hifihifihifihifihifi'
>>> a=('hifi ') * 5
>>> a
'hifi hifi hifi hifi hifi '
>>> a[5]
'h'
>>> a[2]
'f'
>>> a=('hifi',) * 5
>>> a
('hifi', 'hifi', 'hifi', 'hifi', 'hifi')
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a[5]
IndexError: tuple index out of range
>>> a[2]
'hifi'
>>> a[1]
'hifi'
>>> x
(5, 2, 4, 6, 7, 9)
>>> min(x)
2
>>> z
(5, 2, 4, 6, 7, 9, 5, 'Max', 52.5, [3, 2])
>>> del(z)
>>> z
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> 
>>> # Sets
>>> a={1,2,5,6,4,7,2}
>>> a
{1, 2, 4, 5, 6, 7}
>>> len(a)
6
>>> a.add(10)
>>> a
{1, 2, 4, 5, 6, 7, 10}
>>> a.add(10)
>>> a
{1, 2, 4, 5, 6, 7, 10}
>>> a.update([11,56,3])
>>> a
{1, 2, 3, 4, 5, 6, 7, 10, 11, 56}
>>> a.remove(11)
>>> a
{1, 2, 3, 4, 5, 6, 7, 10, 56}
>>> a.discard(5)
>>> a
{1, 2, 3, 4, 6, 7, 10, 56}
>>> a.remove(100)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a.remove(100)
KeyError: 100
>>> a.discard(100)
>>> a
{1, 2, 3, 4, 6, 7, 10, 56}
>>> len(a)
8
>>> a.pop()
1
>>> a
{2, 3, 4, 6, 7, 10, 56}
>>> a.pop()
2
>>> a
{3, 4, 6, 7, 10, 56}
>>> name={25,'Tom',52.6,2}
>>> name
{'Tom', 25, 2, 52.6}
>>> name.clear()
>>> name
set()
>>> del name
>>> name
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name=set(('max','tom',56))
>>> name
{'max', 56, 'tom'}
>>> type(max)
<class 'builtin_function_or_method'>
>>> z=set([4,5,6,2,8])
>>> z
{2, 4, 5, 6, 8}
>>> type(z)
<class 'set'>
>>> a
{3, 4, 6, 7, 10, 56}
>>> b={10,45,65,85,25,35}
>>> b
{65, 35, 10, 45, 85, 25}
>>> a | b
{65, 3, 4, 35, 6, 7, 10, 45, 85, 56, 25}
>>> a.union()
{3, 4, 6, 7, 56, 10}
>>> a.union(b)
{65, 3, 4, 35, 6, 7, 10, 45, 85, 56, 25}
>>> a & b
{10}
>>> a.intersection
<built-in method intersection of set object at 0x01433568>
>>> 

9
>>> a.intersection(b)
{10}
>>> a - b
{3, 4, 6, 7, 56}
>>> b - a
{65, 35, 45, 85, 25}
>>> a.difference(b)
{3, 4, 6, 7, 56}
>>> b.difference(a)
{65, 35, 45, 85, 25}
>>> a ^ b
{65, 3, 4, 6, 7, 85, 25, 35, 45, 56}
>>> b ^ a
{65, 3, 4, 6, 7, 85, 25, 35, 45, 56}
>>> a.symmetric_difference(b)
{65, 3, 4, 6, 7, 85, 25, 35, 45, 56}
>>> 
>>> dir(a)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 