#!/usr/bin/python3
"""
Exports into a JSON file all tasks and
all employees they are associated with
in a dictionary of lists of dictionaries.
"""


if __name__ == '__main__':
    import json
    import requests

    # URL to make API requests from
    url = 'https://jsonplaceholder.typicode.com'

    # Employee information
    employee = requests.get('{}/users'.format(url))
    user_list = employee.json()

    # Todo list information
    task_list = []

    for user in user_list:
        tasks = requests.get('{}/todos?userId={}'.format(url, user.get('id')))
        task_list += tasks.json()

    # JSON formatted data to insert into JSON file
    json_dict = {user.get('id'): [{"task": task.get('title'),
                                   "completed": task.get('completed'),
                                   "username": user.get('username')}
                                  for task in task_list
                                  if user.get('id') == task.get('userId')]
                 for user in user_list}

    # Export json data into json file
    with open('todo_all_employees.json', 'w') as fp:
        json.dump(json_dict, fp)
