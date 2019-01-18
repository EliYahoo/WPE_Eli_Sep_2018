"""
This week, we implemented a version of the Unix "tee" command. The key to solving this week's exercise was understanding that a file object is just another object: You can pass file objects as arguments to functions, you can return them from functions, and you can store them in larger data structures. Moreover, because file objects are objects, you can invoke methods on them and do all sorts of other magic.

First and foremost, let's consider that you can open and close files using objects. So if I want to read from files, one line at a time, then I can do so as follows:
    f1 = open('/etc/passwd')
    f2 = open('/Users/reuven/.zshrc')
    for one_file in [f1, f2]:
        for one_line in one_file:
            print(one_line, end='')

In the above code, we create two file objects ("f1" and "f2"), and put them into a list. We then iterate over that list, reading (and printing) each line from each of the file objects. Note that because each time we read a line from a file object we get the entire line, including the newline character, printing almost always ends up having a blank line between each printed line -- one newline from "print", and one newline from the string.

In this exercise, we weren't interested in reading from files, but rather in writing to them. We can do something similar to the above, though:
    f1 = open('out1.txt', 'w')
    f2 = open('out2.txt', 'w')
    for one_file in [f1, f2]:
        one_file.write('abc\n')
        one_file.write('def\n')
        one_file.write('ghi\n')
        one_file.close()

In this case, I've opened the two files for writing. This means that I can invoke the "write" method (three times) on each file object. Once I'm done writing to the file, I then close it, ensuring that everything I wrote has been flushed to disk -- and also ensuring that we cannot write to the file again.

For the exercise, we needed to create a class that would accept multiple file-like objects (i.e., files and things such as StringIO) upon creation. We can implement this with the following code:
    class Tee(object):
        def __init__(self, *files):
            self.files = files

In other words, with this code in place, we can create a new instance of Tee as follows:
    import sys
    f1 = open('/tmp/tee1.txt', 'w')
    f2 = open('/tmp/tee2.txt', 'w')
    t = Tee(sys.stdout, f1, f2)

(Note that sys.stdout is always available implicitly from within any Python program -- but in order to name it and pass it, you need to "import sys".)

This is fine, but now we need to implement the "write" method. The idea is that if we "write" to our object, the string will be written to all file-like objects. We can do this with a "for" loop:
    def write(self, text):
        for one_file in self.files:
            one_file.write(text)

Now, writing to our object will write to all of the files. Note that the files won't be closed or flushed, however; we'll get to that in a moment.

While it's nice to write a single string to a file, it's sometimes more convenient and reasonable to write a list of strings. For that, most file-like objects provide a "writelines" method. We'll implement it in our own object as follows:
    def writelines(self, lines):
        for one_file in self.files:
            one_file.writelines(lines)

We now have three methods -- __init__, write, and writelines. Here's how the class looks for now:
    class Tee(object):
        def __init__(self, *files):
            self.files = files

        def write(self, text):
            for one_file in self.files:
                one_file.write(text)

        def writelines(self, lines):
            for one_file in self.files:
                one_file.writelines(lines)

This works, but there's still something missing: How and when do we close and flush these objects?  We can, of course, implement "flush" and "close" methods. But a more Pythonic way to handle this is to use a "context manager". That is, we can implement methods such that if someone puts our object in a "with" statement, then the __enter__ method is invoked when entering the block, and the __exit__ method is invoked upon exiting the block and/or when an exception is raised.

The __enter__ method doesn't need to do much in our case, other than return the Tee object that it was handled. If you don't return that object, then nothing will be bound to the variable in the "with" statement, and we'll be in trouble.  Here's how that method will look:
    def __enter__(self):
        return self

The __exit__ method is a bit trickier, in that it needs to be defined to take a few parameters. These parameters are there so that if an exception is raised, you can handle it, knowing the exception type, message, and so forth. The three parameters that we need, in addition to "self", are for the exception type (class), the exception message (value) and the traceback.

We're going to ignore exceptions, which means that all of these parameters will be ignored in the body of our method. Instead, we will use __exit__ as an opportunity to close each of the file-like objects in self.files. Here's how it can look:
    def __exit__(self, exc_type, exc_val, exc_tb):
        for one_file in self.files:
            one_file.close()

We can now use "Tee" in code that looks like this:
    f3 = open('/tmp/tee3.txt', 'w')
    f4 = open('/tmp/tee4.txt', 'w')

    with Tee(f3, f4) as t2:
        t2.write('!!!xyz\n')
        t2.write('???xyz\n')

After we're done using the "Tee" object, we can be sure that f3 and f4 are both closed, because the __exit__ method will be invoked at the end of the block.

We now have a useful class that with a few methods can simplify the rest of our code, and even use the "with" statement in a Pythonic way.

Questions? Comments? Suggestions? Go to the forum!

I'll be back tomorrow with a new exercise.

Reuven
"""

#!/usr/bin/env python3

import sys

class Tee(object):
    def __init__(self, *files):
        self.files = files

    def write(self, text):
        for one_file in self.files:
            one_file.write(text)

    def writelines(self, lines):
        for one_file in self.files:
            one_file.writelines(lines)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for one_file in self.files:
            one_file.close()

if __name__ == '__main__':
    f1 = open('/tmp/tee1.txt', 'w')
    f2 = open('/tmp/tee2.txt', 'w')
    t = Tee(sys.stdout, f1, f2)

    t.write('abc\n')
    t.write('def\n')
    t.write('ghi\n')

    f3 = open('/tmp/tee3.txt', 'w')
    f4 = open('/tmp/tee4.txt', 'w')

    with Tee(f3, f4) as t2:
        t2.write('!!!xyz\n')
        t2.write('???xyz\n')