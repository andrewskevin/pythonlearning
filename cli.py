# from functions import read_todos, write_todos
import functions
import time

# testing program by Kevin


now = time.strftime("%B %d, %Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space chars from it.
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.read_todos("todos.txt")

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.read_todos("todos.txt")

        # new_todo = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.read_todos("todos.txt")

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except (ValueError, IndexError):
            print("This command only takes the number of the todo.\n" "This works for the complete command too.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.read_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"The todo that was removed was {todo_to_remove}."
            print(message)

        except (ValueError, IndexError):
            print("The todo list is presently small or big to support that item.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
# This code only works if the while loop has ended.
print("Bye!")
