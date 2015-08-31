# Files

## Persistence

Most of the programs we have seen so far are transient in the sense that they run for a short time and produce some output, but when they end, their data disappears. If you run the program again, it starts with a clean slate.

Other programs are [persistent](glossary.ipynb#persistent): they run for a long time
(or all the time); they keep at least some of their data in permanent storage (a hard drive, for example); and if they shut down and restart, they pick up where they left off.

Examples of persistent programs are operating systems, which run pretty much whenever a computer is on, and web servers, which run all the time, waiting for requests to come in on the network.

One of the simplest ways for programs to maintain their data is by reading and writing text files. We have already seen programs that read text files; in this chapter we will see programs that write them.

An alternative is to store the state of the program in a database. In this chapter I will present a simple database and a module, ``pickle``, that makes it easy to store program data.

## Reading and writing

A text file is a sequence of characters stored on a permanent medium like a hard drive, flash memory, or CD-ROM.

To write a file, you have to open it with mode `'w'` as a second parameter:

fout = open('output.txt', 'w')
print fout

If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful! If the file doesn’t exist, a new one is created.

The ``write`` method puts data into the file.

line1 = "This here's the wattle,\n"
fout.write(line1)

Again, the file object keeps track of where it is, so if you call ``write`` again, it adds the new data to the end.

line2 = "the emblem of our land.\n"
fout.write(line2)

When you are done writing, you have to close the file.

fout.close()

## Format operator

The argument of ``write`` has to be a string, so if we want to put other values in a file, we have to convert them to strings. The easiest way to do that is with ``str``:

x = 52
f.write(str(x))

An alternative is to use the [format operator](glossary.ipynb#format_operator), ``%``. When applied to integers, ``%`` is the modulus operator. But when the first operand is a string, ``%`` is the format operator.

The first operand is the [format string](glossary.ipynb#format_string), which contains one or more [format sequences](glossary.ipynb#format_sequence), which specify how the second operand is formatted. The result is a string.

For example, the format sequence `'%d'` means that the second operand should be formatted as an integer (``d`` stands for “decimal”):

camels = 42
'%d' % camels

The result is the string `'42'`, which is not to be confused with the integer value ``42``.

A format sequence can appear anywhere in the string, so you can embed a value in a sentence:

camels = 42
'I have spotted %d camels.' % camels

If there is more than one format sequence in the string, the second argument has to be a tuple. Each format sequence is matched with an element of the tuple, in order.

The following example uses `'%d'` to format an integer, `'%g'` to format a floating-point number (don’t ask why), and `'%s'` to format a string:

'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

The number of elements in the tuple has to match the number of format sequences in the string. Also, the types of the elements have to match the format sequences:

'%d %d %d' % (1, 2)

'%d' % 'dollars'

In the first example, there aren’t enough elements; in the second, the element is the wrong type.

The format operator is powerful, but it can be difficult to use. You can read more about it at
<http://docs.python.org/2/library/stdtypes.html#string-formatting>.

## Filenames and paths

Files are organized into [directories](glossary.ipynb#directory) (also called
“folders”). Every running program has a “current directory,” which is the default directory for most operations. For example, when you open a file for reading, Python looks for it in the current directory.

The ``os`` module provides functions for working with files and directories (“os” stands for “operating system”). ``os.getcwd`` returns the name of the current directory:

import os
cwd = os.getcwd()
print cwd

``cwd`` stands for “current working directory.” The result in this example is ``/home/dinsdale``, which is the home directory of a user named ``dinsdale``.

A string like ``cwd`` that identifies a file is called a [path](glossary.ipynb#path). A [relative path](glossary.ipynb#relative_path) starts from the current directory; an [absolute path](glossary.ipynb#absolute_path) starts from the topmost directory in the file system.

The paths we have seen so far are simple filenames, so they are relative to the current directory. To find the absolute path to a file, you can use ``os.path.abspath``:

os.path.abspath('aux/memo.txt')

``os.path.exists`` checks whether a file or directory exists:

os.path.exists('aux/memo.txt')

If it exists, ``os.path.isdir`` checks whether it’s a directory:

os.path.isdir('aux/memo.txt')

os.path.isdir('music')

Similarly, ``os.path.isfile`` checks whether it’s a file.

``os.listdir`` returns a list of the files (and other directories) in the given directory:

os.listdir(cwd)

To demonstrate these functions, the following example “walks” through a directory, prints the names of all the files, and calls itself recursively on all the directories.

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print path
        else:
            walk(path)

``os.path.join`` takes a directory and a file name and joins them into a complete path.

The ``os`` module provides a function called ``walk`` that is similar to this one but more versatile. Read the documentation and use it to print the names of the files in a given directory and its subdirectories.

## Catching exceptions

A lot of things can go wrong when you try to read and write files. If you try to open a file that doesn’t exist, you get an ``IOError``:

fin = open('bad_file')

If you don’t have permission to access a file:

fout = open('/etc/passwd', 'w')

And if you try to open a directory for reading, you get

fin = open('/home')

To avoid these errors, you could use functions like ``os.path.exists`` and ``os.path.isfile``, but it would take a lot of time and code to check all the possibilities (if
“``Errno 21``” is any indication, there are at least 21 things that can go wrong).

It is better to go ahead and try—and deal with problems if they happen—which is exactly what the ``try`` statement does. The syntax is similar to an ``if`` statement:

try:
    fin = open('bad_file')
    for line in fin:
        print line
    fin.close()
except IOError:
    print 'Something went wrong.'

Python starts by executing the ``try`` clause. If all goes well, it skips the ``except`` clause and proceeds. If an exception occurs, it jumps out of the ``try`` clause and executes the ``except`` clause.

Handling an exception with a ``try`` statement is called [catching](glossary.ipynb#catch) an exception. In this example, the ``except`` clause prints an error message that is not very helpful. In general, catching an exception gives you a chance to fix the problem, or try again, or at least end the program gracefully.

Write a function called ``sed`` that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files, your program should catch the exception, print an error message, and exit.

## Databases

A [database](glossary.ipynb#database) is a file that is organized for storing data. Most databases are organized like a dictionary in the sense that they map from keys to values. The biggest difference is that the database is on disk (or other permanent storage), so it persists after the program ends.

The module ``anydbm`` provides an interface for creating and updating database files. As an example, I’ll create a database that contains captions for image files.

Opening a database is similar to opening other files:

import anydbm
db = anydbm.open('captions.db', 'c')

The mode `'c'` means that the database should be created if it doesn’t already exist. The result is a database object that can be used (for most operations) like a dictionary. If you create a new item, ``anydbm`` updates the database file.

db['cleese.png'] = 'Photo of John Cleese.'

When you access one of the items, ``anydbm`` reads the file:

print db['cleese.png']

If you make another assignment to an existing key, ``anydbm`` replaces the old value:

db['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
print db['cleese.png']

Many dictionary methods, like ``keys`` and ``items``, also work with database objects. So does iteration with a ``for`` statement.

for key in db:
    print key

As with other files, you should close the database when you are done:

db.close()

## Pickling

A limitation of ``anydbm`` is that the keys and values have to be strings. If you try to use any other type, you get an error.

The ``pickle`` module can help. It translates almost any type of object into a string suitable for storage in a database, and then translates strings back into objects.

``pickle.dumps`` takes an object as a parameter and returns a string representation (``dumps`` is short for “dump string”):

import pickle
t = [1, 2, 3]
pickle.dumps(t)

The format isn’t obvious to human readers; it is meant to be easy for ``pickle`` to interpret. ``pickle.loads`` (“load string”) reconstitutes the object:

t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print t2

Although the new object has the same value as the old, it is not (in general) the same object:

t1 == t2

t1 is t2

In other words, pickling and then unpickling has the same effect as copying the object.

You can use ``pickle`` to store non-strings in a database. In fact, this combination is so common that it has been encapsulated in a module called ``shelve``.

The file `code/anagram_sets.py`, creates a dictionary that maps from a sorted string of letters to the list of words that can be spelled with those letters. For example, ``’opst’`` maps to the list .

Write a module that imports `anagram_sets` and provides two new functions: `store_anagrams` should store the anagram dictionary in a
“shelf;” `read_anagrams` should look up a word and return a list of its anagrams.

## Pipes

Most operating systems provide a command-line interface, also known as a *shell*. Shells usually provide commands to navigate the file system and launch applications. For example, in Unix you can change directories with ``cd``, display the contents of a directory with ``ls``, and launch a web browser by typing (for example) ``firefox``.

Any program that you can launch from the shell can also be launched from Python using a *pipe*. A pipe is an object that represents a running program.

For example, the Unix command ``ls -l`` normally displays the contents of the current directory (in long format). You can launch ``ls`` with ``os.popen``:

cmd = 'ls -l'
fp = os.popen(cmd)

The argument is a string that contains a shell command. The return value is an object that behaves just like an open file. You can read the output from the ``ls`` process one line at a time with ``readline`` or get the whole thing at once with ``read``:

res = fp.read()

When you are done, you close the pipe like a file:

stat = fp.close()
print stat

The return value is the final status of the ``ls`` process; ``None`` means that it ended normally (with no errors).

For example, most Unix systems provide a command called ``md5sum`` that reads the contents of a file and computes a
“checksum.” You can read about MD5 at
<http://en.wikipedia.org/wiki/Md5>. This command provides an efficient way to check whether two files have the same contents. The probability that different contents yield the same checksum is very small (that is, unlikely to happen before the universe collapses).

You can use a pipe to run ``md5sum`` from Python and get the result:

filename = 'book.tex'
cmd = 'md5sum ' + filename
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print res

print stat

In a large collection of MP3 files, there may be more than one copy of the same song, stored in different directories or with different file names. The goal of this exercise is to search for duplicates.

1.  Write a program that searches a directory and all of its
    subdirectories, recursively, and returns a list of complete paths
    for all files with a given suffix (like ``.mp3``). Hint:
    ``os.path`` provides several useful functions for
    manipulating file and path names.

2.  To recognize duplicates, you can use ``md5sum`` to compute
    a “checksum” for each files. If two files have the same checksum,
    they probably have the same contents.

3.  To double-check, you can use the Unix command ``diff``.

## Writing modules

Any file that contains Python code can be imported as a module. For example, suppose you have a file named ``wc.py`` with the following code:

%%writefile wc.py
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print linecount('wc.py')

If you run this program, it reads itself and prints the number of lines in the file, which is 7. You can also import it like this:

import wc

Now you have a module object ``wc``:

print wc

That provides a function called `linecount`:

wc.linecount('wc.py')

So that’s how you write modules in Python.

The only problem with this example is that when you import the module it executes the test code at the bottom. Normally when you import a module, it defines new functions but it doesn’t execute them.

Programs that will be imported as modules often use the following idiom:

    if __name__ == '__main__':
        print linecount('wc.py')

`__name__` is a built-in variable that is set when the program starts. If the program is running as a script, `__name__` has the value `__main__`; in that case, the test code is executed. Otherwise, if the module is being imported, the test code is skipped.

Type this example into a file named ``wc.py`` and run it as a script. Then run the Python interpreter and ``import wc``. What is the value of `__name__` when the module is being imported?

Warning: If you import a module that has already been imported, Python does nothing. It does not re-read the file, even if it has changed.

If you want to reload a module, you can use the built-in function ``reload``, but it can be tricky, so the safest thing to do is restart the interpreter and then import the module again.

## Debugging

When you are reading and writing files, you might run into problems with whitespace. These errors can be hard to debug because spaces, tabs and newlines are normally invisible:

s = '1 2\t 3\n 4'
print s

The built-in function ``repr`` can help. It takes any object as an argument and returns a string representation of the object. For strings, it represents whitespace characters with backslash sequences:

print repr(s)

This can be helpful for debugging.

One other problem you might run into is that different systems use different characters to indicate the end of a line. Some systems use a newline, represented `\n`. Others use a return character, represented `\r`. Some use both. If you move files between different systems, these inconsistencies might cause problems.

For most systems, there are applications to convert from one format to another. You can find them (and read more about this issue) at
<http://en.wikipedia.org/wiki/Newline>. Or, of course, you could write one yourself.
