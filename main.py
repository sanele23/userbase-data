from argparse import ArgumentParser
import csv
import json
from pprint import pprint
import requests


def read():
    product_list_url = 'http://sam-user-activity.eu-west-1.elasticbeanstalk.com/'
    response = requests.get(product_list_url)

    return response.json()


def preview(data):
    pprint(data)


# save data to csv file
def save(data):
    with open('userbase.csv', 'w') as f:
        field_names = ['date', 'no_of_users']
        writer = csv.DictWriter(f, fieldnames=field_names)

        writer.writeheader()
        for row in data.json():
            writer.writerow(row)


# pass argument to the command line
if __name__ == '__main__':
    parser = ArgumentParser(
        description='A command line tool for interacting with our API')
    parser.add_argument('-r', '--read', action='store_true',
                        help='Sends a GET request to the product API.')
    parser.add_argument('-p', '--preview', action='store_true',
                        help='Shows us a preview of the data.')
    parser.add_argument('-s', '--save', action='store_true',
                        help='Save data as csv file.')
    args = parser.parse_args()

    if args.read:
        read()
    if args.preview:
        preview(read())
    else:
        print('Use the -h or --help flags for help')