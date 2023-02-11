FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the to-do items in it"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    """Open a text file and write the to-do items in it"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_args)
