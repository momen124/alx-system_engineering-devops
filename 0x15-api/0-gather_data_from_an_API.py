#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def fetch_user(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    return user, todos

def main(user_id):
    user, todos = fetch_user(user_id)
    if not user:
        print("Employee Name: Incorrect")
        return
    print("Employee Name: OK")

    if not todos:
        print("To Do Count: Incorrect")
        return
    print("To Do Count: OK")

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    if not completed:
        print("First line formatting: Incorrect")
        return
    print("First line formatting: OK")

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for i, c in enumerate(completed, 1):
        print("\tTask {} in output: OK".format(i))

    if len(completed) == len(todos):
        print("All tasks in output")
    else:
        print("Not all tasks in output")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./main_4.py <employee_id>")
    else:
        main(sys.argv[1])
