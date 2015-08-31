# Iteration

## Multiple assignment

As you may have discovered, it is legal to make more than one assignment to the same variable. A new assignment makes an existing variable refer to a new value (and stop referring to the old value).

bruce = 5
print bruce,
bruce = 7
print bruce

The output of this program is ``5 7``, because the first time ``bruce`` is printed, its value is 5, and the second time, its value is 7. The comma at the end of the first ``print`` statement suppresses the newline, which is why both outputs appear on the same line.

<a href='#fig.assign2'>Figure 1</a> shows what [multiple assignment](glossary.ipynb#multiple_assignment) looks like in a state diagram.

With multiple assignment it is especially important to distinguish between an assignment operation and a statement of equality. Because Python uses the equal sign (``=``) for assignment, it is tempting to interpret a statement like ``a = b`` as a statement of equality. It is not!

First, equality is a symmetric relation and assignment is not. For example, in mathematics, if $a=7$ then $7=a$. But in Python, the statement ``a = 7`` is legal and ``7 = a`` is not.

Furthermore, in mathematics, a statement of equality is either true or false, for all time. If $a=b$ now, then $a$ will always equal $b$. In Python, an assignment statement can make two variables equal, but they don’t have to stay that way:

a = 5
b = a    # a and b are now equal
a = 3    # a and b are no longer equal

The third line changes the value of ``a`` but does not change the value of ``b``, so they are no longer equal.

Although multiple assignment is frequently helpful, you should use it with caution. If the values of variables change frequently, it can make the code difficult to read and debug.

<a name='fig.assign2'></a>
<img src='figs/assign2.png'/>

## Updating variables

One of the most common forms of multiple assignment is an [update](glossary.ipynb#update), where the new value of the variable depends on the old.

x = 0
x = x + 1

This means “get the current value of ``x``, add one, and then update ``x`` with the new value.”

If you try to update a variable that doesn’t exist, you get an error, because Python evaluates the right side before it assigns a value to ``x``:

y = y + 1

Before you can update a variable, you have to [initialize](glossary.ipynb#initialization) it, usually with a simple assignment:

y = 0
y = y + 1

Updating a variable by adding 1 is called an [increment](glossary.ipynb#increment); subtracting 1 is called a [decrement](glossary.ipynb#decrement).

## The ``while`` statement

Computers are often used to automate repetitive tasks. Repeating identical or similar tasks without making errors is something that computers do well and people do poorly.

We have seen two programs, ``countdown`` and `print_n`, that use recursion to perform repetition, which is also called [iteration](glossary.ipynb#iteration). Because iteration is so common, Python provides several language features to make it easier. One is the ``for`` statement - we’ll get back to that later.

Another is the ``while`` statement. Here is a version of ``countdown`` that uses a ``while`` statement:

def countdown(n):
    while n > 0:
        print n
        n = n-1
    print 'Blastoff!'

You can almost read the ``while`` statement as if it were English. It means, “While ``n`` is greater than 0, display the value of ``n`` and then reduce the value of ``n`` by 1. When you get to 0, display the word ``Blastoff!``”

More formally, here is the flow of execution for a ``while`` statement:

1.  Evaluate the condition, yielding ``True`` or
    ``False``.

2.  If the condition is false, exit the ``while`` statement and
    continue execution at the next statement.

3.  If the condition is true, execute the body and then go back to step
    1.

This type of flow is called a *loop* because the third step loops back around to the top.

The body of the loop should change the value of one or more variables so that eventually the condition becomes false and the loop terminates. Otherwise the loop will repeat forever, which is called an [infinite loop](glossary.ipynb#infinite_loop). An endless source of amusement for computer scientists is the observation that the directions on shampoo,
“Lather, rinse, repeat,” are an infinite loop.

In the case of ``countdown``, we can prove that the loop terminates because we know that the value of ``n`` is finite, and we can see that the value of ``n`` gets smaller each time through the loop, so eventually we have to get to 0. In other cases, it is not so easy to tell:

def sequence(n):
    while n != 1:
        print n,
        if n%2 == 0:        # n is even
            n = n/2
        else:               # n is odd
            n = n*3+1

The condition for this loop is ``n != 1``, so the loop will continue until ``n`` is ``1``, which makes the condition false.

Each time through the loop, the program outputs the value of ``n`` and then checks whether it is even or odd. If it is even, ``n`` is divided by 2. If it is odd, the value of ``n`` is replaced with ``n*3+1``. For example, if the argument passed to ``sequence`` is 3, the resulting sequence is 3, 10, 5, 16, 8, 4, 2, 1.

Since ``n`` sometimes increases and sometimes decreases, there is no obvious proof that ``n`` will ever reach 1, or that the program terminates. For some particular values of ``n``, we can prove termination. For example, if the starting value is a power of two, then the value of ``n`` will be even each time through the loop until it reaches 1. The previous example ends with such a sequence, starting with 16.

The hard question is whether we can prove that this program terminates for *all positive values* of ``n``. So far, no one has been able to prove it *or* disprove it! (See
<http://en.wikipedia.org/wiki/Collatz_conjecture>.)

Rewrite the function `print_n` from [Recursion](conditionals_and_recursion.ipynb#recursion) using iteration instead of recursion.

## ``break``

Sometimes you don’t know it’s time to end a loop until you get half way through the body. In that case you can use the ``break`` statement to jump out of the loop.

For example, suppose you want to take input from the user until they type ``done``. You could write:

while True:
    line = raw_input('> ')
    if line == 'done':
        break
    print line

print 'Done!'

The loop condition is ``True``, which is always true, so the loop runs until it hits the break statement.

Each time through, it prompts the user with an angle bracket. If the user types ``done``, the ``break`` statement exits the loop. Otherwise the program echoes whatever the user types and goes back to the top of the loop.

This way of writing ``while`` loops is common because you can check the condition anywhere in the loop (not just at the top) and you can express the stop condition affirmatively (“stop when this happens”) rather than negatively (“keep going until that happens.”).

## Square roots

Loops are often used in programs that compute numerical results by starting with an approximate answer and iteratively improving it.

For example, one way of computing square roots is Newton’s method. Suppose that you want to know the square root of $a$. If you start with almost any estimate, $x$, you can compute a better estimate with the following formula:

$$y = \frac{x + a/x}{2}$$ For example, if $a$ is 4 and $x$ is 3:

a = 4.0
x = 3.0
y = (x + a/x) / 2
print y

Which is closer to the correct answer ($\sqrt{4} = 2$). If we repeat the process with the new estimate, it gets even closer:

x = y
y = (x + a/x) / 2
print y

After a few more updates, the estimate is almost exact:

x = y
y = (x + a/x) / 2
print y

x = y
y = (x + a/x) / 2
print y


In general we don’t know ahead of time how many steps it takes to get to the right answer, but we know when we get there because the estimate stops changing:

x = y
y = (x + a/x) / 2
print y

x = y
y = (x + a/x) / 2
print y


When ``y == x``, we can stop. Here is a loop that starts with an initial estimate, ``x``, and improves it until it stops changing:

while True:
    print x
    y = (x + a/x) / 2
    if y == x:
        break
    x = y

For most values of ``a`` this works fine, but in general it is dangerous to test ``float`` equality. Floating-point values are only approximately right: most rational numbers, like $1/3$, and irrational numbers, like $\sqrt{2}$, can’t be represented exactly with a ``float``.

Rather than checking whether ``x`` and ``y`` are exactly equal, it is safer to use the built-in function ``abs`` to compute the absolute value, or magnitude, of the difference between them:

    if abs(y - x) < epsilon:
        break

Where `epsilon` has a value like ``0.0000001`` that determines how close is close enough.

Encapsulate this loop in a function called `square_root` that takes ``a`` as a parameter, chooses a reasonable value of ``x``, and returns an estimate of the square root of ``a``.

## Algorithms

Newton’s method is an example of an [algorithm](glossary.ipynb#algorithm): it is a mechanical process for solving a category of problems (in this case, computing square roots).

It is not easy to define an algorithm. It might help to start with something that is not an algorithm. When you learned to multiply single-digit numbers, you probably memorized the multiplication table. In effect, you memorized 100 specific solutions. That kind of knowledge is not algorithmic.

But if you were “lazy,” you probably cheated by learning a few tricks. For example, to find the product of $n$ and 9, you can write $n-1$ as the first digit and $10-n$ as the second digit. This trick is a general solution for multiplying any single-digit number by 9. That’s an algorithm!

Similarly, the techniques you learned for addition with carrying, subtraction with borrowing, and long division are all algorithms. One of the characteristics of algorithms is that they do not require any intelligence to carry out. They are mechanical processes in which each step follows from the last according to a simple set of rules.

In my opinion, it is embarrassing that humans spend so much time in school learning to execute algorithms that, quite literally, require no intelligence.

On the other hand, the process of designing algorithms is interesting, intellectually challenging, and a central part of what we call programming.

Some of the things that people do naturally, without difficulty or conscious thought, are the hardest to express algorithmically. Understanding natural language is a good example. We all do it, but so far no one has been able to explain *how* we do it, at least not in the form of an algorithm.

## Debugging

As you start writing bigger programs, you might find yourself spending more time debugging. More code means more chances to make an error and more place for bugs to hide.

One way to cut your debugging time is “debugging by bisection.” For example, if there are 100 lines in your program and you check them one at a time, it would take 100 steps.

Instead, try to break the problem in half. Look at the middle of the program, or near it, for an intermediate value you can check. Add a ``print`` statement (or something else that has a verifiable effect) and run the program.

If the mid-point check is incorrect, there must be a problem in the first half of the program. If it is correct, the problem is in the second half.

Every time you perform a check like this, you halve the number of lines you have to search. After six steps (which is fewer than 100), you would be down to one or two lines of code, at least in theory.

In practice it is not always clear what the “middle of the program” is and not always possible to check it. It doesn’t make sense to count lines and find the exact midpoint. Instead, think about places in the program where there might be errors and places where it is easy to put a check. Then choose a spot where you think the chances are about the same that the bug is before or after the check.
