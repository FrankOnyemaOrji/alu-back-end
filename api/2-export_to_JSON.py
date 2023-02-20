#!/usr/bin/python3
""" Library to gather data from an API """

import json
import requests
import sys

""" Function to gather data from an API """

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user_info = requests.request("GET", url).json()
    todo_info = requests.request("GET", todo).json()

    employee_name = user_info.get("name")

    todo_info_sorted = [
        dict(zip(["task", "completed", "username"], 
        [task.get["title"], task.get["completed"], employee_name]))
        for task in todo_info]

    user = {str(employee_id): todo_info_sorted}
    with open(str(employee_id) + '.json', "w") as f:
        f.write(json.dumps(user))
