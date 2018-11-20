'''
    Topics:
        f-strings - https://realpython.com/python-f-strings/#old-school-string-formatting-in-python
'''
import random


def create_math_problems(output):
    for x in range(100):
        print("{}{}{}{}".format(*[random.randint(-40,40) for x in range(4)]))
        print(random.choice(['+','-']))

def main():
    str = ""
    create_math_problems(str)

if __name__ == "__main__":
    main()