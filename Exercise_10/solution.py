'''
Topics:
    namedtuple - creates class
    defaultdict - init value with something default, for example an empty list.
                  Then it's methods can be used, without another initiation:
                    self.tables_and_guests[new_table_number].append(person)
    Sorting a dict into a list, multiple sorting.
    Counter - creates a dict of values and their count
'''

from collections import namedtuple, Counter


Person = namedtuple('Person', ['first_name','last_name'])

class TableFull(Exception):
    def __init__(self, message):
        super().__init__(message)

class GuestList:
    max_at_table = 10

    def __init__(self):
        self.arrangement = {}
        self.count = None

    def __len__(self):
        return self.arrangement.__len__()

    def assign(self, person, table):
        if self.count and table in self.count.keys() and self.count[table] == 0:
            raise TableFull(f"table {table} is full, can't assign more people'")
        self.arrangement[person] = table
        self.free_space()

    def table(self, table_number):
        return [person for (person,table) in self.arrangement.items() if table == table_number]

    def unassigned(self):
        return [person for (person, table) in self.arrangement.items() if table is None]

    def free_space(self):
        if self.arrangement == {}:
            return {}
        else:
            self.count = {x:self.max_at_table-y for x,y in Counter(self.arrangement.values()).items()}
            return self.count

    def guests(self):
        return sorted(self.arrangement.keys(),key= lambda g: (self.arrangement[g],
                                                              g.last_name,
                                                              g.first_name))