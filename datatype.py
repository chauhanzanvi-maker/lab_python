Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x="hello world"
print(type(x))
<class 'str'>
x=20
print(type(x))
<class 'int'>
x=20.5
print(type(x))
<class 'float'>
x=1j
>>> print(type(x))
<class 'complex'>
>>> x=["zanvi","shruti","shreya"]
>>> print(type(x))
<class 'list'>
>>> x=("zanvi","shruti","shreya")
>>> print(type(x))
<class 'tuple'>
>>> x=range(6)
>>> print(type(x))
<class 'range'>
>>> x=frozenset({"zanvi","shruti","shreya"})
>>> print(type(x))
<class 'frozenset'>
>>> x=x={"name":"zanvi","age":18}
>>> print(type(x))
<class 'dict'>
>>> x={"zanvi","shruti","shreya"}
>>> print(type(x))
<class 'set'>
>>> x=True
>>> print(type(x))
<class 'bool'>
>>> x=b"hello"
>>> print(type(x))
<class 'bytes'>
>>> x=bytearray(5)
>>> print(type(x))
<class 'bytearray'>
>>> x=None
>>> print(type(x))
<class 'NoneType'>
>>> x=memoryview(bytes(5))
>>> print(type(x))
<class 'memoryview'>
