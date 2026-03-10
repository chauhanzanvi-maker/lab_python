Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #5)pop()-remove and return last element
>>> from array import array
>>> arr=array('i',[10,20,30,40])
>>> x=arr.pop()
>>> print("removed:",x)
removed: 40
>>> print(arr)
array('i', [10, 20, 30])
>>> #6)index(x)-find index of element
>>> from array import array
>>> arr=array('i',[10,20,30,40])
>>> print(arr.index(30))
2
>>> #7)count occurrence
>>> from array import array
>>> arr=array('i',[10,20,30,20,40])
>>> print(arr.count(20))
2
>>> #8)reverse()-reverse array
>>> from array import array
>>> arr=array('i',[10,20,30,40])
>>> arr.reverse()
>>> print(arr)
array('i', [40, 30, 20, 10])
