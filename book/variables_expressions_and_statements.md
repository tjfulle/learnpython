# Variables, expressions and statements

## Values and types

A [value](glossary.ipynb#value) is one of the basic things a program works with, like a letter or a number. The values we have seen so far are ``1``, ``2``, and `'Hello, World!'`.

These values belong to different [types](glossary.ipynb#type): ``2`` is an integer, and `'Hello, World!'` is a [string](glossary.ipynb#string), so-called because it contains a “string” of letters. You (and the interpreter) can identify strings because they are enclosed in quotation marks.

If you are not sure what type a value has, the interpreter can tell you.

type('Hello, World!')

type(17)


Not surprisingly, strings belong to the type ``str`` and integers belong to the type ``int``. Less obviously, numbers with a decimal point belong to a type called ``float``, because these numbers are represented in a format called [floating-point](glossary.ipynb#floatingpoint).

type(3.2)


What about values like `'17'` and `'3.2'`? They look like numbers, but they are in quotation marks like strings.

type('17')

type('3.2')


They’re strings.

When you type a large integer, you might be tempted to use commas between groups of three digits, as in ``1,000,000``. This is not a legal integer in Python, but it is legal:

1,000,000
    (1, 0, 0)

Well, that’s not what we expected at all! Python interprets ``1,000,000`` as a comma-separated sequence of integers. This is the first example we have seen of a semantic error: the code runs without producing an error message, but it doesn’t do the “right” thing.

## Variables

One of the most powerful features of a programming language is the ability to manipulate [variables](glossary.ipynb#variable). A variable is a name that refers to a value.

An [assignment statement](glossary.ipynb#assignment) creates new variables and gives them values:

message = 'And now for something completely different'
n = 17
pi = 3.1415926535897932

This example makes three assignments. The first assigns a string to a new variable named ``message``; the second gives the integer ``17`` to ``n``; the third assigns the (approximate) value of $\pi$ to ``pi``.

A common way to represent variables on paper is to write the name with an arrow pointing to the variable’s value. This kind of figure is called a [state diagram](glossary.ipynb#state_diagram) because it shows what state each of the variables is in (think of it as the variable’s state of mind). Figure [fig.state2] shows the result of the previous example.

<img src='figs/state2.png'/>

The type of a variable is the type of the value it refers to.

type(message)

type(n)

type(pi)


## Variable names and keywords

Programmers generally choose names for their variables that are meaningful—they document what the variable is used for.

Variable names can be arbitrarily long. They can contain both letters and numbers, but they have to begin with a letter. It is legal to use uppercase letters, but it is a good idea to begin variable names with a lowercase letter (you’ll see why later).

The underscore character, `_`, can appear in a name. It is often used in names with multiple words, such as `my_name` or `airspeed_of_unladen_swallow`.

If you give a variable an illegal name, you get a syntax error:

76trombones = 'big parade'
    SyntaxError: invalid syntax
more@ = 1000000
    SyntaxError: invalid syntax
class = 'Advanced Theoretical Zymurgy'
    SyntaxError: invalid syntax

``76trombones`` is illegal because it does not begin with a letter. ``more@`` is illegal because it contains an illegal character, ``@``. But what’s wrong with ``class``?

It turns out that ``class`` is one of Python’s [keywords](glossary.ipynb#keyword). The interpreter uses keywords to recognize the structure of the program, and they cannot be used as variable names.

Python 2 has 31 keywords:

    and       del       from      not       while
    as        elif      global    or        with
    assert    else      if        pass      yield
    break     except    import    print
    class     exec      in        raise
    continue  finally   is        return
    def       for       lambda    try

In Python 3, ``exec`` is no longer a keyword, but ``nonlocal`` is.

You might want to keep this list handy. If the interpreter complains about one of your variable names and you don’t know why, see if it is on this list.

## Operators and operands

[Operators](glossary.ipynb#operator) are special symbols that represent computations like addition and multiplication. The values the operator is applied to are called [operands](glossary.ipynb#operand).

The operators ``+``, ``-``, ``*``, ``/`` and ``**`` perform addition, subtraction, multiplication, division and exponentiation, as in the following examples:

hour = 1
minute = 34
20+32
hour-1
hour*60+minute
minute/60
5**2
(5+9)*(15-7)

In some other languages, `^` is used for exponentiation, but in Python it is a bitwise operator called XOR. I won’t cover bitwise operators in this book, but you can read about them at
<http://wiki.python.org/moin/BitwiseOperators>.

In Python 2, the division operator might not do what you expect:

minute = 59
minute/60

The value of ``minute`` is 59, and in conventional arithmetic 59 divided by 60 is 0.98333, not 0. The reason for the discrepancy is that Python is performing [floor division](glossary.ipynb#floor_division). When both of the operands are integers, the result is also an integer; floor division chops off the fraction part, so in this example it rounds down to zero.

In Python 3, the result of this division is a ``float``. The new operator ``//`` performs floor division.

If either of the operands is a floating-point number, Python performs floating-point division, and the result is a ``float``:

minute/60.0


## Expressions and statements

An [expression](glossary.ipynb#expression) is a combination of values, variables, and operators. A value all by itself is considered an expression, and so is a variable, so the following are all legal expressions (assuming that the variable ``x`` has been assigned a value):

x = 1
x + 17

A [statement](glossary.ipynb#statement) is a unit of code that the Python interpreter can execute. We have seen two kinds of statement: print and assignment.

Technically an expression is also a statement, but it is probably simpler to think of them as different things. The important difference is that an expression has a value; a statement does not.

## Interactive mode and script mode

One of the benefits of working with an interpreted language is that you can test bits of code in interactive mode before you put them in a script. But there are differences between interactive mode and script mode that can be confusing.

For example, if you are using Python as a calculator, you might type

miles = 26.2
miles * 1.61

The first line assigns a value to ``miles``, but it has no visible effect. The second line is an expression, so the interpreter evaluates it and displays the result. So we learn that a marathon is about 42 kilometers.

But if you type the same code into a script and run it, you get no output at all. In script mode an expression, all by itself, has no visible effect. Python actually evaluates the expression, but it doesn’t display the value unless you tell it to:

miles = 26.2
print miles * 1.61

This behavior can be confusing at first.

A script usually contains a sequence of statements. If there is more than one statement, the results appear one at a time as the statements execute.

For example, the script

print 1
x = 2
print x

The assignment statement produces no output.

Type the following statements in the Python interpreter to see what they do:

x = 5
x + 1

Now put the same statements into a script and run it. What is the output? Modify the script by transforming each expression into a print statement and then run it again.

## Order of operations

When more than one operator appears in an expression, the order of evaluation depends on the [rules of precedence](glossary.ipynb#rules_of_precedence). For mathematical operators, Python follows mathematical convention. The acronym **PEMDAS** is a useful way to remember the rules:

-   **P**arentheses have the highest precedence and can be
    used to force an expression to evaluate in the order you want. Since
    expressions in parentheses are evaluated first, ``2 *
    (3-1)`` is 4, and ``(1+1)**(5-2)`` is 8. You can
    also use parentheses to make an expression easier to read, as in
    ``(minute * 100) / 60``, even if it doesn’t change the
    result.

-   **E**xponentiation has the next highest precedence, so
    ``2**1+1`` is 3, not 4, and ``3*1**3`` is 3,
    not 27.

-   **M**ultiplication and **D**ivision have
    the same precedence, which is higher than **A**ddition
    and **S**ubtraction, which also have the same
    precedence. So ``2*3-1`` is 5, not 4, and
    ``6+4/2`` is 8, not 5.

-   Operators with the same precedence are evaluated from left to right
    (except exponentiation). So in the expression ``degrees / 2 *
    pi``, the division happens first and the result is multiplied
    by ``pi``. To divide by $2 \pi$, you can use parentheses or
    write ``degrees / 2 / pi``.

I don’t work very hard to remember rules of precedence for other operators. If I can’t tell by looking at the expression, I use parentheses to make it obvious.

## String operations

In general, you can’t perform mathematical operations on strings, even if the strings look like numbers, so the following are illegal:

'2'-'1'

'eggs'/'easy'

'third'*'a charm'

The ``+`` operator works with strings, but it might not do what you expect: it performs [concatenation](glossary.ipynb#concatenate), which means joining the strings by linking them end-to-end. For example:

first = 'throat'
second = 'warbler'
print first + second

The output of this program is ``throatwarbler``.

The operator also works on strings; it performs repetition. For example, `'Spam'*3` is `'SpamSpamSpam'`. If one of the operands is a string, the other has to be an integer.

This use of ``+`` and makes sense by analogy with addition and multiplication. Just as ``4*3`` is equivalent to ``4+4+4``, we expect `'Spam'*3` to be the same as `'Spam'+'Spam'+'Spam'`, and it is. On the other hand, there is a significant way in which string concatenation and repetition are different from integer addition and multiplication. Can you think of a property that addition has that string concatenation does not?

## Comments

As programs get bigger and more complicated, they get more difficult to read. Formal languages are dense, and it is often difficult to look at a piece of code and figure out what it is doing, or why.

For this reason, it is a good idea to add notes to your programs to explain in natural language what the program is doing. These notes are called [comments](glossary.ipynb#comment), and they start with the `#` symbol:

# compute the percentage of the hour that has elapsed
percentage = (minute * 100) / 60

In this case, the comment appears on a line by itself. You can also put comments at the end of a line:

percentage = (minute * 100) / 60     # percentage of an hour

Everything from the ``\#`` to the end of the line is ignored—it has no effect on the program.

Comments are most useful when they document non-obvious features of the code. It is reasonable to assume that the reader can figure out *what* the code does; it is much more useful to explain *why*.

This comment is redundant with the code and useless:

v = 5     # assign 5 to v

This comment contains useful information that is not in the code:

v = 5     # velocity in meters/second.

Good variable names can reduce the need for comments, but long names can make complex expressions hard to read, so there is a tradeoff.

## Debugging

At this point the syntax error you are most likely to make is an illegal variable name, like ``class`` and ``yield``, which are keywords, or `odd~job` and `US$`, which contain illegal characters.

If you put a space in a variable name, Python thinks it is two operands without an operator:

bad name = 5
    SyntaxError: invalid syntax

For syntax errors, the error messages don’t help much. The most common messages are ``SyntaxError: invalid syntax`` and ``SyntaxError: invalid token``, neither of which is very informative.

The runtime error you are most likely to make is a “use before def;” that is, trying to use a variable before you have assigned a value. This can happen if you spell a variable name wrong:

principal = 327.68
interest = principle * rate
    NameError: name 'principle' is not defined

Variables names are case sensitive, so ``LaTeX`` is not the same as ``latex``.

At this point the most likely cause of a semantic error is the order of operations. For example, to evaluate $\frac{1}{2 \pi}$, you might be tempted to write

1.0 / 2.0 * pi

But the division happens first, so you would get $\pi / 2$, which is not the same thing! There is no way for Python to know what you meant to write, so in this case you don’t get an error message; you just get the wrong answer.
