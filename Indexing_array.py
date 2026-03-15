Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> print(arr[0])
10
>>> print(arr[2])
30
>>> print(arr[4])
50
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> print(arr[-1])
50
>>> print(arr[-2])
40
>>> print(arr[-5])
10
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> arr[2]=35
>>> print(arr)
array('i', [10, 20, 35, 40, 50])
>>> from array import array
>>> arr=array('i',[10,20,30])
>>> print(arr[5])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(arr[5])
IndexError: array index out of range
