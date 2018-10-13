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