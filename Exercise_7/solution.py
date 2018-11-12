'''
Topics:
    Passing functions as arguments
'''

import os

def func_to_dir(dir, func):
    valid_results = {}
    error_results = {}

    for file_elem in os.listdir(dir):
        try:
            valid_results[file_elem] = func(file_elem)
        except Exception as e:
            error_results[file_elem] = e

    return valid_results, error_results

good, bad = func_to_dir("../Exercise_5",os.stat)
print("The end")