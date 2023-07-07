FILEPATH = "todos.txt"


def read_todos(filepath=FILEPATH):
    """ Reads a text file and returns a list of the todo items in it."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(write_what, filepath=FILEPATH):
    """ Writes todo items in a text file."""
    with open(filepath, 'w') as file:
        file.writelines(write_what)


if __name__ == "__main__":
    print("functions.py")



