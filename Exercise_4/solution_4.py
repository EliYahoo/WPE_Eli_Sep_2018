import time
import re

logfilename = '../Exercise_3/mini-access-log.txt'


class LogDicts:
    def __init__(self, log_file_name):
        with open(log_file_name, 'r') as f:
            self.dict_list = [re.match(r'(?P<ip_address>(?:\d{1,3}\.){3}\d{1,3})'
                                       r'(?:.*)(?:\[(?P<timestamp>[^\]]*))(?:.*)'
                                       r'(?P<request>GET[^\"]*)', line).groupdict() for line in f]

    def dicts(self, key=None):
        if key is None:
            return self.dict_list
        elif key in self.dict_list:
            return self.dict_list[key]

        return None

    def iterdicts(self, key=None):
        for d in self.dict_list:
            yield d

    # returns the dict with the earliest timestamp
    def latest(self):
        latest_time_dict = self.dict_list[-1]
        latest_time = time.mktime(time.strptime(latest_time_dict['timestamp'], "%d/%b/%Y:%H:%M:%S %z"))

        for d in self.dict_list:
            if time.mktime(time.strptime(d['timestamp'], "%d/%b/%Y:%H:%M:%S %z")) > latest_time:
                latest_time_dict = d
                latest_time = time.mktime(time.strptime(latest_time_dict['timestamp'], "%d/%b/%Y:%H:%M:%S %z"))

        return latest_time_dict

    # returns the dict with the latest timestamp
    def earliest(self):
        earliest_time_dict = self.dict_list[0]
        earliest_time = time.mktime(time.strptime(earliest_time_dict['timestamp'], "%d/%b/%Y:%H:%M:%S %z"))

        for d in self.dict_list:
            if time.mktime(time.strptime(d['timestamp'], "%d/%b/%Y:%H:%M:%S %z")) < earliest_time:
                earliest_time_dict = d
                earliest_time = time.mktime(time.strptime(earliest_time_dict['timestamp'], "%d/%b/%Y:%H:%M:%S %z"))

        return earliest_time_dict


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
