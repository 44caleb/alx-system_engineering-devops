#!/usr/bin/python3
"""requests data from an api and exports in csv format"""


import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    file_name = "{}.csv".format(user_id)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response1 = requests.get(user_url)
    user = response1.json()
    
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    response2 = requests.get(todo_url, params={"userId": user_id})
    tasks = response2.json()

    rows = []
    for task in tasks:
        record = {"USER_ID": "{}".format(user["id"]),
                "USERNAME": "{}".format(user["username"]), 
                "TASK_COMPLETED_STATUS": "{}".format(task["completed"]),
                "TASK_TITLE": "{}".format(task["title"])}
        rows.append(record)
    with open(file_name, "w") as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames)
        writer.writerows(rows)
