# Lists

## A list is a sequence

Like a string, a [list](glossary.ipynb#list) is a sequence of values. In a string, the values are characters; in a list, they can be any type. The values in a list are called [elements](glossary.ipynb#element) or sometimes *items*.

There are several ways to create a new list; the simplest is to enclose the elements in square brackets (`[` and `]`):

[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']

The first example is a list of four integers. The second is a list of three strings. The elements of a list don’t have to be the same type. The following list contains a string, a float, an integer, and (lo!) another list:

['spam', 2.0, 5, [10, 20]]

A list within another list is [nested](glossary.ipynb#nested_list).

A list that contains no elements is called an empty list; you can create one with empty brackets, `[]`.

As you might expect, you can assign list values to variables:

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print cheeses, numbers, empty

## Lists are mutable

The syntax for accessing the elements of a list is the same as for accessing the characters of a string—the bracket operator. The expression inside the brackets specifies the index. Remember that the indices start at 0:

print cheeses[0]

Unlike strings, lists are mutable. When the bracket operator appears on the left side of an assignment, it identifies the element of the list that will be assigned.

numbers = [17, 123]
numbers[1] = 5
print numbers

The one-eth element of ``numbers``, which used to be 123, is now 5.

You can think of a list as a relationship between indices and elements. This relationship is called a [mapping](glossary.ipynb#mapping); each index “maps to” one of the elements. <a href='#fig.liststate'>Figure 1</a> shows the state diagram for ``cheeses``, ``numbers`` and ``empty``:

<a name='fig.liststate'></a>
<img src='figs/liststate.png'/>

Lists are represented by boxes with the word “list” outside and the elements of the list inside. ``cheeses`` refers to a list with three elements indexed 0, 1 and 2. ``numbers`` contains two elements; the diagram shows that the value of the second element has been reassigned from 123 to 5. ``empty`` refers to a list with no elements.

List indices work the same way as string indices:

-   Any integer expression can be used as an index.

-   If you try to read or write an element that does not exist, you get
    an ``IndexError``.

-   If an index has a negative value, it counts backward from the end of
    the list.

The ``in`` operator also works on lists.

cheeses = ['Cheddar', 'Edam', 'Gouda']
'Edam' in cheeses

'Brie' in cheeses

## Traversing a list

The most common way to traverse the elements of a list is with a ``for`` loop. The syntax is the same as for strings:

for cheese in cheeses:
    print cheese

This works well if you only need to read the elements of the list. But if you want to write or update the elements, you need the indices. A common way to do that is to combine the functions ``range`` and ``len``:

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

This loop traverses the list and updates each element. ``len`` returns the number of elements in the list. ``range`` returns a list of indices from 0 to $n-1$, where $n$ is the length of the list. Each time through the loop ``i`` gets the index of the next element. The assignment statement in the body uses ``i`` to read the old value of the element and to assign the new value.

A ``for`` loop over an empty list never executes the body:

for x in []:
    print 'This never happens.'

Although a list can contain another list, the nested list still counts as a single element. The length of this list is four:

a = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
len(a)

## List operations

The ``+`` operator concatenates lists:

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print c

Similarly, the operator repeats a list a given number of times:

[0] * 4

[1, 2, 3] * 3

The first example repeats four times. The second example repeats the list three times.

## List slices

The slice operator also works on lists:

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]

t[:4]

t[3:]

If you omit the first index, the slice starts at the beginning. If you omit the second, the slice goes to the end. So if you omit both, the slice is a copy of the whole list.

t[:]

Since lists are mutable, it is often useful to make a copy before performing operations that fold, spindle or mutilate lists.

A slice operator on the left side of an assignment can update multiple elements:

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print t

## List methods

Python provides methods that operate on lists. For example, ``append`` adds a new element to the end of a list:

t = ['a', 'b', 'c']
t.append('d')
print t

``extend`` takes a list as an argument and appends all of the elements:

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print t1

This example leaves ``t2`` unmodified.

``sort`` arranges the elements of the list from low to high:

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print t

List methods are all void; they modify the list and return ``None``. If you accidentally write ``t = t.sort()``, you will be disappointed with the result.

## Map, filter and reduce

To add up all the numbers in a list, you can use a loop like this:

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

``total`` is initialized to 0. Each time through the loop, ``x`` gets one element from the list. The ``+=`` operator provides a short way to update a variable. This [augmented assignment statement](glossary.ipynb#augmented_assignment):

    total += x

is equivalent to:

    total = total + x

As the loop executes, ``total`` accumulates the sum of the elements; a variable used this way is sometimes called an [accumulator](glossary.ipynb#accumulator).

Adding up the elements of a list is such a common operation that Python provides it as a built-in function, ``sum``:

t = [1, 2, 3]
sum(t)

An operation like this that combines a sequence of elements into a single value is sometimes called [reduce](glossary.ipynb#reduce).

Write a function called `nested_sum` that takes a nested list of integers and add up the elements from all of the nested lists.

Sometimes you want to traverse one list while building another. For example, the following function takes a list of strings and returns a new list that contains capitalized strings:

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

``res`` is initialized with an empty list; each time through the loop, we append the next element. So ``res`` is another kind of accumulator.

An operation like `capitalize_all` is sometimes called a [map](glossary.ipynb#map) because it “maps” a function (in this case the method ``capitalize``) onto each of the elements in a sequence.

Use `capitalize_all` to write a function named `capitalize_nested` that takes a nested list of strings and returns a new nested list with all strings capitalized.

Another common operation is to select some of the elements from a list and return a sublist. For example, the following function takes a list of strings and returns a list that contains only the uppercase strings:

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

``isupper`` is a string method that returns ``True`` if the string contains only upper case letters.

An operation like `only_upper` is called a [filter](glossary.ipynb#filter) because it selects some of the elements and filters out the others.

Most common list operations can be expressed as a combination of map, filter and reduce. Because these operations are so common, Python provides language features to support them, including the built-in function ``map`` and an operator called a “list comprehension.”

Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the $i$th element is the sum of the first
$i+1$ elements from the original list. For example, the cumulative sum of is .

## Deleting elements

There are several ways to delete elements from a list. If you know the index of the element you want, you can use ``pop``:

t = ['a', 'b', 'c']
x = t.pop(1)
print t

print x

``pop`` modifies the list and returns the element that was removed. If you don’t provide an index, it deletes and returns the last element.

If you don’t need the removed value, you can use the ``del`` operator:

t = ['a', 'b', 'c']
del t[1]
print t

If you know the element you want to remove (but not the index), you can use ``remove``:

t = ['a', 'b', 'c']
t.remove('b')
print t

The return value from ``remove`` is ``None``.

To remove more than one element, you can use ``del`` with a slice index:

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print t

As usual, the slice selects all the elements up to, but not including, the second index.

Write a function called `middle` that takes a list and returns a new list that contains all but the first and last elements. So `middle([1,2,3,4])` should return `[2,3]`.

Write a function called `chop` that takes a list, modifies it by removing the first and last elements, and returns ``None``.

## Lists and strings

A string is a sequence of characters and a list is a sequence of values, but a list of characters is not the same as a string. To convert from a string to a list of characters, you can use ``list``:

s = 'spam'
t = list(s)
print t

Because ``list`` is the name of a built-in function, you should avoid using it as a variable name. I also avoid ``l`` because it looks too much like ``1``. So that’s why I use ``t``.

The ``list`` function breaks a string into individual letters. If you want to break a string into words, you can use the ``split`` method:

s = 'pining for the fjords'
t = s.split()
print t

An optional argument called a [delimiter](glossary.ipynb#delimiter) specifies which characters to use as word boundaries. The following example uses a hyphen as a delimiter:

s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)

``join`` is the inverse of ``split``. It takes a list of strings and concatenates the elements. ``join`` is a string method, so you have to invoke it on the delimiter and pass the list as a parameter:

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)

In this case the delimiter is a space character, so ``join`` puts a space between words. To concatenate strings without spaces, you can use the empty string, `''`, as a delimiter.

## Objects and values

If we execute these assignment statements:

a = 'banana'
b = 'banana'

We know that ``a`` and ``b`` both refer to a string, but we don’t know whether they refer to the *same* string. There are two possible states, shown in <a href='#fig.list1'>Figure 2</a>.

<a name='fig.list1'></a>
<img src='figs/list1.png'/>

In one case, ``a`` and ``b`` refer to two different objects that have the same value. In the second case, they refer to the same object.

To check whether two variables refer to the same object, you can use the ``is`` operator.

a = 'banana'
b = 'banana'
a is b

In this example, Python only created one string object, and both ``a`` and ``b`` refer to it.

But when you create two lists, you get two objects:

a = [1, 2, 3]
b = [1, 2, 3]
a is b

So the state diagram looks like <a href='#fig.list2'>Figure 3</a>

<a name='fig.list2'></a>
<img src='figs/list2.png'/>

In this case we would say that the two lists are [equivalent](glossary.ipynb#equivalent), because they have the same elements, but not [identical](glossary.ipynb#identical), because they are not the same object. If two objects are identical, they are also equivalent, but if they are equivalent, they are not necessarily identical.

Until now, we have been using “object” and “value” interchangeably, but it is more precise to say that an object has a value. If you execute , you get a list object whose value is a sequence of integers. If another list has the same elements, we say it has the same value, but it is not the same object.

## Aliasing

If ``a`` refers to an object and you assign ``b = a``, then both variables refer to the same object:

a = [1, 2, 3]
b = a
b is a

The state diagram looks like <a href='#fig.list3'>Figure 4</a>

<a name='fig.list3'></a>
<img src='figs/list3.png'/>

The association of a variable with an object is called a [reference](glossary.ipynb#reference). In this example, there are two references to the same object.

An object with more than one reference has more than one name, so we say that the object is [aliased](glossary.ipynb#aliasing).

If the aliased object is mutable, changes made with one alias affect the other:

b[0] = 17
print a

Although this behavior can be useful, it is error-prone. In general, it is safer to avoid aliasing when you are working with mutable objects.

For immutable objects like strings, aliasing is not as much of a problem. In this example:

a = 'banana'
b = 'banana'

It almost never makes a difference whether ``a`` and ``b`` refer to the same string or not.

## List arguments

When you pass a list to a function, the function gets a reference to the list. If the function modifies a list parameter, the caller sees the change. For example, `delete_head` removes the first element from a list:

def delete_head(t):
    del t[0]

Here’s how it is used:

letters = ['a', 'b', 'c']
delete_head(letters)
print letters

The parameter ``t`` and the variable ``letters`` are aliases for the same object. The stack diagram looks like <a href='#fig.stack5'>Figure 5</a>

<a name='fig.stack5'></a>
<img src='figs/stack5.png'/>

Since the list is shared by two frames, I drew it between them.

It is important to distinguish between operations that modify lists and operations that create new lists. For example, the ``append`` method modifies a list, but the ``+`` operator creates a new list:

t1 = [1, 2]
t2 = t1.append(3)
print t1

print t2

t3 = t1 + [4]
print t3

This difference is important when you write functions that are supposed to modify lists. For example, this function *does not* delete the head of a list:

def bad_delete_head(t):
    t = t[1:]              # WRONG!

The slice operator creates a new list and the assignment makes ``t`` refer to it, but none of that has any effect on the list that was passed as an argument.

An alternative is to write a function that creates and returns a new list. For example, ``tail`` returns all but the first element of a list:

def tail(t):
    return t[1:]

This function leaves the original list unmodified. Here’s how it is used:

letters = ['a', 'b', 'c']
rest = tail(letters)
print rest

## Debugging

Careless use of lists (and other mutable objects) can lead to long hours of debugging. Here are some common pitfalls and ways to avoid them:

1.  Don’t forget that most list methods modify the argument and return
    ``None``. This is the opposite of the string methods, which
    return a new string and leave the original alone.

    If you are used to writing string code like this:

        word = word.strip()

    It is tempting to write list code like this:

        t = t.sort()           # WRONG!

    Because ``sort`` returns ``None``, the next
    operation you perform with ``t`` is likely to fail.

    Before using list methods and operators, you should read the
    documentation carefully and then test them in interactive mode. The
    methods and operators that lists share with other sequences (like
    strings) are documented at
    <http://docs.python.org/2/library/stdtypes.html#typesseq>. The
    methods and operators that only apply to mutable sequences are
    documented at
    <http://docs.python.org/2/library/stdtypes.html#typesseq-mutable>.

2.  Pick an idiom and stick with it.

    Part of the problem with lists is that there are too many ways to do
    things. For example, to remove an element from a list, you can use
    ``pop``, ``remove``, ``del``, or even a
    slice assignment.

    To add an element, you can use the ``append`` method or the
    ``+`` operator. Assuming that ``t`` is a list and
    ``x`` is a list element, these are right:

        t.append(x)
        t = t + [x]

    And these are wrong:

        t.append([x])          # WRONG!
        t = t.append(x)        # WRONG!
        t + [x]                # WRONG!
        t = t + x              # WRONG!

    Try out each of these examples in interactive mode to make sure you
    understand what they do. Notice that only the last one causes a
    runtime error; the other three are legal, but they do the wrong
    thing.

3.  Make copies to avoid aliasing.

    If you want to use a method like ``sort`` that modifies the
    argument, but you need to keep the original list as well, you can
    make a copy.

        orig = t[:]
        t.sort()

    In this example you could also use the built-in function
    ``sorted``, which returns a new, sorted list and leaves the
    original alone. But in that case you should avoid using
    ``sorted`` as a variable name!
