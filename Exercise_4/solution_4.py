"""
Topics:
    sorted()
    filter()
        sort according to key parameter
    lambda functions
"""
import time
import re

logfilename = '../Exercise_3/mini-access-log.txt'


def convert_time(dict_item):
    return time.mktime(time.strptime(dict_item['timestamp'], "%d/%b/%Y:%H:%M:%S %z"))


class LogDicts:
    def __init__(self, log_file_name):
        with open(log_file_name, 'r') as f:
            self.dict_list = [re.match(r'(?P<ip_address>(?:\d{1,3}\.){3}\d{1,3})'
                                       r'(?:.*)(?:\[(?P<timestamp>[^\]]*))(?:.*)'
                                       r'(?P<request>GET[^\"]*)', line).groupdict() for line in f]

    def dicts(self, key=None):
        if key:
            return sorted(self.dict_list, key=key)

        return self.dict_list

    def iterdicts(self, key=None):
        if key:
            for item in sorted(self.dict_list, key):
                yield item
        else:
            for item in self.dict_list:
                yield item

    # returns the dict with the earliest timestamp
    def latest(self):
        return max(self.dict_list, key=convert_time)

    # returns the dict with the latest timestamp
    def earliest(self):
        return min(self.dict_list, key=convert_time)

    def for_ip(self, ip_address, key=None):
        if key:
            return sorted(list(filter(lambda item: item['ip_address'] == ip_address, self.dict_list)), key=key)

        return list(filter(lambda item: item['ip_address'] == ip_address, self.dict_list))

    def for_request(self, request, key=None):
        if key:
            return sorted(list(filter(lambda item: request in item['request'], self.dict_list)), key)

        return list(filter(lambda item: request in item['request'], self.dict_list))


def main():
    ld = LogDicts(logfilename)

    for d in ld.iterdicts():
        print(d['timestamp'])

    earlist_dict = ld.earliest()
    print("Earliest " + earlist_dict['timestamp'])

    latest_dict = ld.latest()
    print("Latest " + latest_dict['timestamp'])


if __name__ == "__main__":
    main()
