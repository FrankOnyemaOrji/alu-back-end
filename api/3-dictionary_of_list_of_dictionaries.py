#!/usr/bin/python3
""" Library to gather data from an API """

import json
import requests

def get_employee_task_data(employee_id):
    """ Function to gather data from an API """
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
    return user

def get_all_employee_ids():
    """ Function to gather all employee ids """
    url = "https://jsonplaceholder.typicode.com/users"
    user_info = requests.request("GET", url).json()
    return [user.get("id") for user in user_info]


if __name__ == "__main__":
    all_employee_ids = get_all_employee_ids()
    for employee_id in all_employee_ids:
        user = get_employee_task_data(employee_id)
        with open(str(employee_id) + '.json', "w") as f:
            f.write(json.dumps(user))
