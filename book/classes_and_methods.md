<div style="background-color: #FFFFFF; margin-right: 10px; padding-bottom: 8px; padding-left: 8px; padding-right: 8px; padding-top: 8px; border: 2px solid black;">

# Classes and methods

Code examples from this chapter are available from
<http://thinkpython.com/code/Time2.py>.

## Object-oriented features

Python is an [object-oriented programming language](glossary.ipynb#object_oriented_language), which means that it provides features that support object-oriented programming.

It is not easy to define object-oriented programming, but we have already seen some of its characteristics:

-   Programs are made up of object definitions and function definitions,
    and most of the computation is expressed in terms of operations on
    objects.

-   Each object definition corresponds to some object or concept in the
    real world, and the functions that operate on that object correspond
    to the ways real-world objects interact.

For example, the ``Time`` class defined in Chapter [time] corresponds to the way people record the time of day, and the functions we defined correspond to the kinds of things people do with times. Similarly, the ``Point`` and ``Rectangle`` classes correspond to the mathematical concepts of a point and a rectangle.

So far, we have not taken advantage of the features Python provides to support object-oriented programming. These features are not strictly necessary; most of them provide alternative syntax for things we have already done. But in many cases, the alternative is more concise and more accurately conveys the structure of the program.

For example, in the ``Time`` program, there is no obvious connection between the class definition and the function definitions that follow. With some examination, it is apparent that every function takes at least one ``Time`` object as an argument.

This observation is the motivation for [methods](glossary.ipynb#method); a method is a function that is associated with a particular class. We have seen methods for strings, lists, dictionaries and tuples. In this chapter, we will define methods for user-defined types.

Methods are semantically the same as functions, but there are two syntactic differences:

-   Methods are defined inside a class definition in order to make the
    relationship between the class and the method explicit.

-   The syntax for invoking a method is different from the syntax for
    calling a function.

In the next few sections, we will take the functions from the previous two chapters and transform them into methods. This transformation is purely mechanical; you can do it simply by following a sequence of steps. If you are comfortable converting from one form to another, you will be able to choose the best form for whatever you are doing.

## Printing objects

In [Time](classes_and_functions.ipynb), we defined a class named ``Time`` and wrote a function named `print_time`:

class Time(object):
    """Represents the time of day."""

def print_time(time):
    print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)

To call this function, you have to pass a ``Time`` object as an argument:

start = Time()
start.hour = 9
start.minute = 45
start.second = 00
print_time(start)

To make `print_time` a method, all we have to do is move the function definition inside the class definition. Notice the change in indentation.

class Time(object):
    def print_time(time):
        print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)

Now there are two ways to call `print_time`. The first (and less common) way is to use function syntax:

Time.print_time(start)

In this use of dot notation, ``Time`` is the name of the class, and `print_time` is the name of the method. ``start`` is passed as a parameter.

The second (and more concise) way is to use method syntax:

start.print_time()

In this use of dot notation, `print_time` is the name of the method
(again), and ``start`` is the object the method is invoked on, which is called the [subject](glossary.ipynb#subject). Just as the subject of a sentence is what the sentence is about, the subject of a method invocation is what the method is about.

Inside the method, the subject is assigned to the first parameter, so in this case ``start`` is assigned to ``time``.

By convention, the first parameter of a method is called ``self``, so it would be more common to write `print_time` like this:

class Time(object):
    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

The reason for this convention is an implicit metaphor:

-   The syntax for a function call, `print_time(start)`, suggests that
    the function is the active agent. It says something like, “Hey
    `print_time`! Here’s an object for you to print.”

-   In object-oriented programming, the objects are the active agents. A
    method invocation like `start.print_time()` says “Hey
    ``start``! Please print yourself.”

This change in perspective might be more polite, but it is not obvious that it is useful. In the examples we have seen so far, it may not be. But sometimes shifting responsibility from the functions onto the objects makes it possible to write more versatile functions, and makes it easier to maintain and reuse code.

<div style="background-color: #FFFFFF; margin-right: 10px; padding-bottom: 8px; padding-left: 8px; padding-right: 8px; padding-top: 8px; border: 2px solid black;">
Rewrite `time_to_int` (from [Prototyping](classes_and_functions.ipynb#prototype)) as a method. It is probably not appropriate to rewrite `int_to_time` as a method; what object you would invoke it on?</div>

## Another example

Here’s a version of ``increment`` (from [Modifiers](classes_and_functions.ipynb#increment)) rewritten as a method:

class Time(object):
    # new increment method
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

This version assumes that `time_to_int` is written as a method. Also, note that it is a pure function, not a modifier.

Here’s how you would invoke ``increment``:

start.print_time()

end = start.increment(1337)
end.print_time()

The subject, ``start``, gets assigned to the first parameter, ``self``. The argument, ``1337``, gets assigned to the second parameter, ``seconds``.

This mechanism can be confusing, especially if you make an error. For example, if you invoke ``increment`` with two arguments, you get:

end = start.increment(1337, 460)

The error message is initially confusing, because there are only two arguments in parentheses. But the subject is also considered an argument, so all together that’s three.

## A more complicated example

`is_after` is slightly more complicated because it takes two Time objects as parameters. In this case it is conventional to name the first parameter ``self`` and the second parameter ``other``:

class Time(object):
    # new is_after method
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

To use this method, you have to invoke it on one object and pass the other as an argument:

end.is_after(start)

One nice thing about this syntax is that it almost reads like English:
“end is after start?”

## The init method

The init method (short for “initialization”) is a special method that gets invoked when an object is instantiated. Its full name is `__init__`
(two underscore characters, followed by ``init``, and then two more underscores). An init method for the ``Time`` class might look like this:

class Time(object):
    # new __init__ method
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)


It is common for the parameters of `__init__` to have the same names as the attributes. The statement

    self.hour = hour

stores the value of the parameter ``hour`` as an attribute of ``self``.

The parameters are optional, so if you call ``Time`` with no arguments, you get the default values.

time = Time()
time.print_time()

If you provide one argument, it overrides ``hour``:

time = Time (9)
time.print_time()

If you provide two arguments, they override ``hour`` and ``minute``.

time = Time(9, 45)
time.print_time()

And if you provide three arguments, they override all three default values.

<div style="background-color: #FFFFFF; margin-right: 10px; padding-bottom: 8px; padding-left: 8px; padding-right: 8px; padding-top: 8px; border: 2px solid black;">
Write an init method for the ``Point`` class that takes ``x`` and ``y`` as optional parameters and assigns them to the corresponding attributes.</div>

## The ``__str__`` method

`__str__` is a special method, like `__init__`, that is supposed to return a string representation of an object.

For example, here is a ``str`` method for Time objects:

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # new __str__ method
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

When you ``print`` an object, Python invokes the ``str`` method:

time = Time(9, 45)
print time

When I write a new class, I almost always start by writing `__init__`, which makes it easier to instantiate objects, and `__str__`, which is useful for debugging.

<div style="background-color: #FFFFFF; margin-right: 10px; padding-bottom: 8px; padding-left: 8px; padding-right: 8px; padding-top: 8px; border: 2px solid black;">
Write a ``str`` method for the ``Point`` class. Create a Point object and print it.</div>

## Operator overloading

By defining other special methods, you can specify the behavior of operators on user-defined types. For example, if you define a method named `__add__` for the ``Time`` class, you can use the ``+`` operator on Time objects.

Here is what the definition might look like:

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    # new __add__ method
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

And here is how you could use it:

start = Time(9, 45)
duration = Time(1, 35)
print start + duration

When you apply the ``+`` operator to Time objects, Python invokes `__add__`. When you print the result, Python invokes `__str__`. So there is quite a lot happening behind the scenes!

Changing the behavior of an operator so that it works with user-defined types is called [operator overloading](glossary.ipynb#operator_overloading). For every operator in Python there is a corresponding special method, like `__add__`. For more details, see
<http://docs.python.org/2/reference/datamodel.html#specialnames>.

<div style="background-color: #FFFFFF; margin-right: 10px; padding-bottom: 8px; padding-left: 8px; padding-right: 8px; padding-top: 8px; border: 2px solid black;">
Write an ``add`` method for the Point class.</div>

## Type-based dispatch

In the previous section we added two Time objects, but you also might want to add an integer to a Time object. The following is a version of `__add__` that checks the type of ``other`` and invokes either `add_time` or ``increment``:

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    # new __add__ method
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

The built-in function ``isinstance`` takes a value and a class object, and returns ``True`` if the value is an instance of the class.

If ``other`` is a Time object, `__add__` invokes `add_time`. Otherwise it assumes that the parameter is a number and invokes ``increment``. This operation is called a [type-based dispatch](glossary.ipynb#typebased_dispatch) because it dispatches the computation to different methods based on the type of the arguments.

Here are examples that use the ``+`` operator with different types:

start = Time(9, 45)
duration = Time(1, 35)
print start + duration

print start + 1337

Unfortunately, this implementation of addition is not commutative. If the integer is the first operand, you get

print 1337 + start

The problem is, instead of asking the Time object to add an integer, Python is asking an integer to add a Time object, and it doesn’t know how to do that. But there is a clever solution for this problem: the special method `__radd__`, which stands for “right-side add.” This method is invoked when a Time object appears on the right side of the ``+`` operator. Here’s the definition:

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    # new __radd__ method
    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

And here’s how it’s used:

print 1337 + start

<div style="background-color: #FFFFFF; margin-right: 10px; padding-bottom: 8px; padding-left: 8px; padding-right: 8px; padding-top: 8px; border: 2px solid black;">
Write an ``add`` method for Points that works with either a Point object or a tuple:<p>
<ul>
  <li>
    If the second operand is a Point, the method should return a new
    Point whose $x$ coordinate is the sum of the $x$ coordinates of the
    operands, and likewise for the $y$ coordinates.
  </li>
  <li>
    If the second operand is a tuple, the method should add the first
    element of the tuple to the $x$ coordinate and the second element to
    the $y$ coordinate, and return a new Point with the result.
  </li>
</ul>
</div>

## Polymorphism

Type-based dispatch is useful when it is necessary, but (fortunately) it is not always necessary. Often you can avoid it by writing functions that work correctly for arguments with different types.

Many of the functions we wrote for strings will actually work for any kind of sequence. For example, in [Dictionaries as counters](dictionaries.ipynb#histogram) we used ``histogram`` to count the number of times each letter appears in a word.

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c]+1
    return d

This function also works for lists, tuples, and even dictionaries, as long as the elements of ``s`` are hashable, so they can be used as keys in ``d``.

t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
histogram(t)

Functions that can work with several types are called [polymorphic](glossary.ipynb#polymorphic). Polymorphism can facilitate code reuse. For example, the built-in function ``sum``, which adds the elements of a sequence, works as long as the elements of the sequence support addition.

Since Time objects provide an ``add`` method, they work with ``sum``:

t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
total = sum([t1, t2, t3])
print total

In general, if all of the operations inside a function work with a given type, then the function works with that type.

The best kind of polymorphism is the unintentional kind, where you discover that a function you already wrote can be applied to a type you never planned for.

## Debugging

It is legal to add attributes to objects at any point in the execution of a program, but if you are a stickler for type theory, it is a dubious practice to have objects of the same type with different attribute sets. It is usually a good idea to initialize all of an object’s attributes in the init method.

If you are not sure whether an object has a particular attribute, you can use the built-in function ``hasattr``.

Another way to access the attributes of an object is through the special attribute `__dict__`, which is a dictionary that maps attribute names
(as strings) and values:

t = Time()
print t.__dict__

For purposes of debugging, you might find it useful to keep this function handy:

def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)

`print_attributes` traverses the items in the object’s dictionary and prints each attribute name and its corresponding value.

The built-in function ``getattr`` takes an object and an attribute name (as a string) and returns the attribute’s value.

## Interface and implementation

One of the goals of object-oriented design is to make software more maintainable, which means that you can keep the program working when other parts of the system change, and modify the program to meet new requirements.

A design principle that helps achieve that goal is to keep interfaces separate from implementations. For objects, that means that the methods a class provides should not depend on how the attributes are represented.

For example, in this chapter we developed a class that represents a time of day. Methods provided by this class include `time_to_int`, `is_after`, and `add_time`.

We could implement those methods in several ways. The details of the implementation depend on how we represent time. In this chapter, the attributes of a ``Time`` object are ``hour``, ``minute``, and ``second``.

As an alternative, we could replace these attributes with a single integer representing the number of seconds since midnight. This implementation would make some methods, like `is_after`, easier to write, but it makes some methods harder.

After you deploy a new class, you might discover a better implementation. If other parts of the program are using your class, it might be time-consuming and error-prone to change the interface.

But if you designed the interface carefully, you can change the implementation without changing the interface, which means that other parts of the program don’t have to change.

Keeping the interface separate from the implementation means that you have to hide the attributes. Code in other parts of the program (outside the class definition) should use methods to read and modify the state of the object. They should not access the attributes directly. This principle is called [information hiding](glossary.ipynb#information_hiding); see
<http://en.wikipedia.org/wiki/Information_hiding>.
