Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #1)len()-number of elements
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> print(len(arr))
5
>>> #2)append(x)-add element at end
>>> from array import array
>>> arr=array('i',[10,20,30])
>>> arr.append(40)
>>> print(arr)
array('i', [10, 20, 30, 40])
>>> #3)insert(pos,x)-insert at position
>>> from array import array
>>> arr=array('i',[10,20,40])
>>> arr.insert(2,30)
>>> print(arr)
array('i', [10, 20, 30, 40])
>>> #4)remove(x)-remove first occurrence
>>> from array import array
>>> arr=array('i',[10,20,30,40])
>>> arr.remove(20)
>>> print(arr)
array('i', [10, 30, 40])
