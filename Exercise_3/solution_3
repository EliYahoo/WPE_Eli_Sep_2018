"""
This week's exercise requires that we take a file, whose lines look like this:
67.218.116.165 - - [30/Jan/2010:00:03:18 +0200] "GET /robots.txt HTTP/1.0" 200 99 "-" "Mozilla/5.0 (Twiceler-0.9 http://www.cuil.com/twiceler/robot.html)"

and turn this file into a list of dictionaries.  Moreover, we're supposed to do this in a function that takes a single argument, namely the filename from which we should read things.

Many newcomers to Python -- and some experienced hands, as well! -- hear that they need to create a list, and immediately think about using a "for" loop, as well as the "list.append" method. But more experienced Python hands realize that if we're going to be iterating over the lines of a file, then we can use a list comprehension. Moreover, if the task is to create a list of dicts, then so long as our list comprehension produces a dict for each input string, we're basically set.

We can thus start with a function that iterates over the contents of a file, and
    def logtodict(filename):
        return [{}
                for line in open(filename)]

The above verison of "logtodict" returns a list of dictionaries. There's just one problem; the dictionary that this function returns is empty.

We could do it all in a single line, at least in theory. But in such cases, I find it's better to invoke a function from within the list comprehension, as follows:
    def logtodict(filename):
        return [line_to_dict(line)
                for line in open(filename)]

In this way, we've broken the problem down: Now we just need to write the line_to_dict function, such that it takes a line from the logfile and returns a dictionary.

Now, when it comes to searching for text inside of strings, I think that regular expressions are generally the best way to go. (I did, after all, write a book about regular expressions!) However, I recognize that regexps are hard for many people to grasp, especially if they don't use them very often. I've thus created two solutions (enclosed below), one which uses regexps and the other of which doesn't.

Let's start with the brute-force parsing, and then we can move onto the one that uses regular expressions.  We basically want to extract three parts of the line:
The IP address, which is the first field
The timestamp, which is the only thing between square brackets ([ and ]) in the string
The HTTP request, which is inside of double quotes and starts with GET
We can use a few different techniques to extract this text from the logfile:

(1) The IP address can be retrieved by using str.split without a parameter. This tells str.split to use whitespace -- any whitespace character (\n, \t, \r, and space), in any quantity, and in any combination -- for its splitting.  The result of str.split is always a list, and thus if we retrieve the first element from the resulting list, we'll get the IP address.  For example:
    In [9]: line.split()[0]
    Out[9]: '67.218.116.165'

(2) The timestamp can be retrieved by using str.index to find the opening square bracket. We can then grab the string starting just after the [ character, and search for the matching ] character. With those indexes in hand, we can then use a slice to retrieve the part of the string that we want.
    In [10]: timestamp_start = line.index('[') + 1
        ...: timestamp_end = line.index(']')
        ...: timestamp = line[timestamp_start:timestamp_end]

    In [11]: timestamp
    Out[11]: '30/Jan/2010:00:03:18 +0200'

(3) We can similarly retrieve the request by looking for " after the end of the timestamp, and then a matching final " after the first one:
    In [12]: request_start = line.index('"') + 1
        ...: request_end = line[request_start:].index('"')
        ...: request = line[request_start:request_start+request_end]

    In [13]: request
    Out[13]: 'GET /robots.txt HTTP/1.0'

With these three in hand, we can now create and our dictionary:
    return {'ip_address': ip_address,
            'timestamp': timestamp,
            'request': request}

The list comprehension will invoke this function once per line. And then the list comprehension will itself return a list of dictionaries.

How could we do this with regular expressions? I wasn't sure if it was best to search three separate time (readable, but slow), or once (less readable, but much more efficient).  I decided that I would write one log regexp, but that I would break it up using re.X (aka re.VERBOSE), and then have the three parts of the regexp on separate lines, commented.

Here's how it looks:
        regexp = r'''
    ((?:\d{1,3}\.){3}\d{1,3})       # IP addresses contain four numbers (each with 1-3 digits)
    .*                              # Junk between IP address and timestamp
    \[([^\]]+)\]                    # Timestamp, defined to be anything between [ and ]
    .*                              # Junk between timestamp and request
    "(GET[^"]+)"                    # Request, starting with GET
    '''

I think that the comments describe what I would say here anyway, so I'll let that be.  I do want to point out that I used a few techniques here that might help you, too:
I used a raw string to define the regexp. That helps to avoid confusion and warnings (especially, but not only, in pytest) when you use \d and other backslashed characters that are special in regexps, but not in Python strings.
I used ?: to ensure that the group surrounding \d{1,3}\., which I created so that {3} would apply to it, would not be numbered. That is, it makes the parentheses into a "non-capturing group."  We do this by putting ?: just after the opening parentheses.
I could have specified the date more carefully. But given that the only occurrence of [ and ] in the logfile was around the timestamp, I decided to be lenient.
I indicated that we were only interested in GET requests, and that the request would be surrounded by " characters. This allowed me to use the same cheap trick with both the timestamp and the request, namely the "[^"]+" regexp pattern, which basically says, "Give me the double quotes, and anything inside of them."
I thought about using named groups, rather than numbered ones.  I love the idea in theory, but in practice I find that it just makes my regexps longer.  However, it makes retrieval much eaiser and more readable, for sure.
If you didn't previously think that re.VERBOSE was a good idea, I hope that you'll consider it now!

Finally, our logtodict function should, under most modern circumstances, return not a list, but rather an iterator. How can we do that? By using a generator expression, rather than a list comprehension. That's accomplished by changing our logtodict function to use regular parentheses, rather than square brackets:

You can discuss this exercise in the forum.  I'll be back tomorrow with exercise #4.

Reuven
"""
#!/usr/bin/env python3

import re

logfilename = 'mini-access-log.txt'

def re_line_to_dict(line):
    regexp = r'''
((?:\d{1,3}\.){3}\d{1,3})       # IP addresses contain four numbers (each with 1-3 digits)
.*                              # Junk between IP address and timestamp
\[([^\]]+)\]                    # Timestamp, defined to be anything between [ and ]
.*                              # Junk between timestamp and request
"(GET[^"]+)"                    # Request, starting with GET
'''
    m = re.search(regexp, line, re.X)

    if m:
        ip_address = m.group(1)
        timestamp = m.group(2)
        request = m.group(3)

    else:
        ip_address = 'No IP address found'
        timestamp = 'No timestamp found'
        request = 'No request found'

    output = {'ip_address': ip_address,
              'timestamp': timestamp,
              'request': request}
    return output


def line_to_dict(line):
    ip_address = line.split()[0]

    timestamp_start = line.index('[') + 1
    timestamp_end = line.index(']')
    timestamp = line[timestamp_start:timestamp_end]

    request_start = line.index('"') + 1
    request_end = line[request_start:].index('"')
    request = line[request_start:request_start+request_end]

    return {'ip_address': ip_address,
            'timestamp': timestamp,
            'request': request}


def logtolist(filename):
    return [line_to_dict(line)
            for line in open(filename)]


for one_item in logtolist(logfilename):
    print(one_item)