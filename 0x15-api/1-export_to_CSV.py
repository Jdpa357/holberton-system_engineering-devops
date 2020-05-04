#!/usr/bin/python3
"""
Returns information about an employee
whose ID is passed into the script.
Exports data in CSV format
"""


if __name__ == '__main__':
    import csv
    import requests
    import sys

    # URL to request from the API
    url = 'https://jsonplaceholder.typicode.com'

    # ID of the user to request
    user_id = sys.argv[1]

    # Employee information
    employee = requests.get('{}/users/{}'.format(url, user_id))
    username = employee.json().get('username')

    # Tasks list information
    tasks = requests.get('{}/todos?userId={}'.format(url, user_id))
    task_list = tasks.json()

    # List of rows to insert into CSV file
    row_list = [[user_id,
                 username,
                 task.get('completed'),
                 task.get('title')]
                for task in task_list]

    # Insert rows into CSV file
    with open('{}.csv'.format(user_id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(row_list)
