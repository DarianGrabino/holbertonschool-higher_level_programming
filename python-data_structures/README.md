# Python - Data Structures: Lists, Tuples
## Lists
Lists are data structures that can store any other type of data, including a list can contain another list, in addition, the number of elements in a list can be modified by removing or adding elements. Brackets are used to define a list, inside these are placed all the elements separated by commas:

```python
grades = [10,9,8,7.5,9]
names = ["Ana","Juan","Sofía","Pablo","Tania"]
mix = [True, 10.5, "abc", [0,1,1]]
```
Lists are iterable and therefore their elements can be accessed by indexing:

```python
names[2]
```
'Sofia'

```python
names[-1]
```
'Tania'

You have the ability to add items to a list using the append method:

```python
names.append("Antonio")
names.append("Ximena")
print(names)
```
['Ana', 'Juan', 'Sofía', 'Pablo', 'Tania', 'Antonio', 'Ximena']

The remove method removes an element from a list:

```python
names.remove("Anna")
print(names)
```
['Juan', 'Sofía', 'Pablo', 'Tania', 'Antonio', 'Ximena']

If the value passed to the remove method does not exist, Python will return a ValueError:

```python
names.remove("George")
-------------------------------------------------- -------------------------
ValueError Traceback (most recent call last)
<ipython-input-91-d983d2559e2f> in <module>()
----> 1 names.remove("Jorge")

ValueError: list.remove(x): x not in list
```

## Tuples
Tuples are sequences of elements similar to lists, the main difference is that tuples cannot be modified directly, that is, a tuple does not have methods such as append or insert that modify the elements of a list.

To define a tuple, the elements are separated by commas and enclosed in parentheses.

```python
colors=("Blue","Green","Red","Yellow","White","Black","Grey")
```

Tuples being iterable can be accessed using the bracket and index notation.

```python
colors[0]
```
'Blue'

```python
colors[-1]
```
'Grey'

```python
colors[3]
```
'Yellow'

If we try to modify any of the elements of the tuple, Python will return a TypeError:

```python
colors[0] = "Coffee"
-------------------------------------------------- -------------------------
TypeError Traceback (most recent call last)
<ipython-input-96-3502c7127536> in <module>()
----> 1 colors[0] = "Coffee"

TypeError: 'tuple' object does not support item assignment
```
