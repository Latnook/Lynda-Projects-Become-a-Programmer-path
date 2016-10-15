Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> stack = list()
>>> stack.append('bill1')
>>> stack.append('bill2')
>>> stack.pop()
'bill2'
>>> stack.append('bill3')
>>> stack.append('bill4')
>>> stack.pop()
'bill4'
>>> stack.pop()
'bill3'
>>> stack.pop()
'bill1'
>>> stack.pop()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    stack.pop()
IndexError: pop from empty list
>>> s
