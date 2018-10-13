"""
Usefull links:
RE tutorial
    https://www.guru99.com/python-regular-expressions-complete-tutorial.html
RE online tester
    https://regex101.com/
RE groups: (), (?:), (?P<>)
    https://stackoverflow.com/questions/18425386/re-findall-not-returning-full-match
    https://stackoverflow.com/questions/10059673/named-regular-expression-group-pgroup-nameregexp-what-does-p-stand-for
Memory efficient way to read file:
    https://stackoverflow.com/questions/8009882/how-to-a-read-large-file-line-by-line-in-python
    https://stackabuse.com/read-a-file-line-by-line-in-python/
"""
import re

def logtolist(logfilename):

    # Read file
    entries_list = []

    with open(logfilename, 'r') as f:
        for line in f:
            # Match RE
            match = re.search(r'(?P<ip_address>(?:\d{1,3}\.){3}\d{1,3})'
                              r'(?:.*)(?:\[(?P<timestamp>[^\]]*))(?:.*)'
                              r'(?P<request>GET[^\"]*)', line)
            entries_list.append(match.groupdict())

    return entries_list