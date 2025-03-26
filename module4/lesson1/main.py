# 1
import requests
from datetime import datetime


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        t_start = datetime.now()
        result = func(*args, **kwargs)
        t_finish = datetime.now()
        execution_time = t_finish - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f"Function completed in "
              f"{execution_time.seconds}s {milliseconds}ms")
        return result
    return wrapper


@measure_execution_time
def send_get_request(url):
    return requests.get(url)


url_address = "https://google.com"
print(send_get_request(url_address))


#2
def requires_admin(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        if user["role"] == "admin":
            return func(*args, **kwargs)
        else:
            raise PermissionError(f"incorrect role \"{user['role']}\"")
    return wrapper


@requires_admin
def delete_user(user, username_to_delete):
    return f"User {username_to_delete} has been deleted by {user['username']}."


admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}

print(delete_user(admin_user, 'Charlie'))
print(delete_user(regular_user, 'Charlie'))