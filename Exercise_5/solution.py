'''
Topics:
    requests package for html requests
    DictWriter - requires fieldnames dict and reads from dicts with the corresponding keys
'''
import csv
import requests

gist_url = 'https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/' \
            '2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json'


def cities_to_csv(file_url, output_csv):
    r = requests.get(file_url)
    j = r.json()

    with open(output_csv, 'w', newline='') as csv_file:
        wr = csv.DictWriter(csv_file, fieldnames=['city', 'state', 'rank', 'population'],
                            extrasaction='ignore', delimiter='\t')
        wr.writerows(j)


def main():
    cities_to_csv(gist_url, "test_output.csv")


if __name__ == "__main__":
    main()