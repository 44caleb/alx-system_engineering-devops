#!/usr/bin/python3
"""gathers data using an API"""


import csv
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    response1 = requests.get(user_url)
    emp_data = response1.json()
    emp_name = emp_data["name"]

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    response2 = requests.get(todo_url, params={"userId": emp_id})
    tasks = response2.json()
    completed = 0
    total = 0
    task_names = []

    for task in tasks:
        task_names.append(task["title"])
        if task["completed"] == True:
            completed += 1
        total += 1

    print("Employee {} is done with tasks({}/{})".format(emp_name, completed, total))
    for task_name in task_names:
        print("\t  {}".format(task_name))
