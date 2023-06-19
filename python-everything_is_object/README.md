# Everything is object
This project is a little bit different than the usual projects. The first part is only questions about Python’s

task 0 What function would you use to print the type of an object?

task 1 How do you get the variable identifier (which is the memory address in the CPython implementation)?

task 2 In the following code, do a and b point to the same object? Answer with Yes or No.
```python
>>> a = 89
>>> b = 100
```

task 3 In the following code, do a and b point to the same object? Answer with Yes or No.
```python
>>> a = 89
>>> b = 89
```

task 4 In the following code, do a and b point to the same object? Answer with Yes or No.
```python
>>> a = 89
>>> b = a
```

task 5 In the following code, do a and b point to the same object? Answer with Yes or No.
```python
>>> a = 89
>>> b = a + 1
```

task 6 What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

task 7 What do these 3 lines print?
```python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

task 8 What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

task 9 What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

task 10 What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

task 11 What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

task 12 What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

task 13 What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

task 14 What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

task 15 What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

task 16 What does this script print?
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

task 17 What does this script print?
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

task 18 What does this script print?
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
task 19 Write a function def copy_list(a_list): that returns a copy of a list.
- The input list can contain any type of objects 
- Your file should be maximum 3-line long (no documentation needed) 
- You are not allowed to import any module

task 20 Is a a tuple? Answer with Yes or No.
```python
a = ()
```

task 21 Is a a tuple? Answer with Yes or No.
```python
a = (1, 2)
```

task 22 Is a a tuple? Answer with Yes or No.
```python
a = (1)
```

task 23 Is a a tuple? Answer with Yes or No.
```python
a = (1, )
```

task 24 What does this script print?
```python
a = (1)
b = (1)
a is b
```

task 25 What does this script print?
```python
a = (1, 2)
b = (1, 2)
a is b
```

task 26 What does this script print?
```python
a = ()
b = ()
a is b
```
task 27 Will the last line of this script print 139926795932424? Answer with Yes or No.

task 28 Will the last line of this script print 139926795932424? Answer with Yes or No
```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```