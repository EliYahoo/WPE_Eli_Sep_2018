'''
Topics:
    nested list comprehensions
    Counter class
    Statistics package - mean etc.

    * To get unique values from list use set
'''
from collections import Counter
from statistics import mean

all_people = [{'name': 'Reuven', 'age': 48, 'hobbies': ['Python', 'cooking', 'reading']},
              {'name': 'Atara', 'age': 17, 'hobbies': ['horses', 'cooking', 'art', 'reading']},
              {'name': 'Shikma', 'age': 15, 'hobbies': ['Python', 'piano', 'cooking', 'reading']},
              {'name': 'Amotz', 'age': 13, 'hobbies': ['biking', 'cooking']}]


def average_age_under(people, maxage):
    age_list = [person['age'] for person in people if person['age'] < maxage]
    return mean(age_list) if age_list else 0


def all_hobbies(people):
    return set([hobby for person in people for hobby in person['hobbies']])


def hobby_counter(people):
    return Counter([hobby for person in people for hobby in person['hobbies']])


def n_most_common(people, n_most_common_hobbies):
    return [elem[0] for elem in
            Counter([hobby for person in people for hobby in person['hobbies']]).most_common(n_most_common_hobbies)]


def main():
    average_age_under(all_people,-1)


if __name__ == "__main__":
    main()