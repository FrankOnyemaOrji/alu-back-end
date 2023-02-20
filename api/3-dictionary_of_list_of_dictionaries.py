#!/usr/bin/python3
""" Library to gather data from an API """

import json
import requests

def get_employee_data(employee_id):
    """ Function"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todo = todo.format(employee_id)

    todo_info = requests.request("GET", todo).json()
    user_info = requests.request("GET", url).json()
    employee_username = user_info.get("username")
    return [
        dict(zip(["task", "completed", "username"],
                 [task["title"], task["completed"], employee_username]))
        for task in todo_info]

    

    

def get_all_employee_ids():
    """ Function to gather all employee ids """
    url = "https://jsonplaceholder.typicode.com/users"
    user_info = requests.request("GET", url).json()
    id = list(map(lambda x: x.get("id"), user_info))
    return id


if __name__ == "__main__":
    all_employee_ids = get_all_employee_ids()
    for employee_id in all_employee_ids:
        user = get_employee_data(employee_id)
        with open(str(employee_id) + '.json', "w") as f:
            f.write(json.dumps(user))
