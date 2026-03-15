Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> print(arr[1:4])
array('i', [20, 30, 40])
>>> print(arr[:3])
array('i', [10, 20, 30])
>>> print(arr[2:])
array('i', [30, 40, 50])
>>> print(arr[:])
array('i', [10, 20, 30, 40, 50])
>>> from array import array
>>> arr=array('i',[10,20,30,40,50,60,70,80])
>>> print(arr[::2])
array('i', [10, 30, 50, 70])
>>> print(arr[1::2])
array('i', [20, 40, 60, 80])
>>> print(arr[::3])
array('i', [10, 40, 70])
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> print(arr[-4:-1])
array('i', [20, 30, 40])
>>> print(arr[-3:])
array('i', [30, 40, 50])
>>> print(arr[:-2])
array('i', [10, 20, 30])
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> print(arr[::-1])
array('i', [50, 40, 30, 20, 10])
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> arr[1:4]=array('i',[25,35,45])
>>> print(arr)
array('i', [10, 25, 35, 45, 50])
