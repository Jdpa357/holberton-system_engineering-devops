#!/usr/bin/python3
"""
Return the information about an employee from an API
whose ID is passed into the script
"""


if __name__ == '__main__':
    import requests
    import sys

    # URL to request from the API
    url = 'https://jsonplaceholder.typicode.com'

    # Employee information
    employee = requests.get('{}/users/{}'.format(url, sys.argv[1]))
    employee_name = employee.json().get('name')

    # Tasks information list
    tasks = requests.get('{}/todos?userId={}'.format(url, sys.argv[1]))
    task_list = tasks.json()
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task.get('completed'))

    # Information printing about the employee task completition
    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                          completed_tasks,
                                                          total_tasks))
    for task in task_list:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
