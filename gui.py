import functions
import PySimpleGUI as sg
import time

sg.theme("black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]


window = sg.Window("My todo app",
                   layout=layout,
                   font=("Helvetica", 20))

while True:
    event, values = window.read(200)
    window["clock"].update(time.strftime("%B %d, %Y %H:%M:%S"))
    match event:
        case "Add":
                todos = functions.read_todos()
                new_todo = values["todo"] + "\n"

                todos.append(new_todo)
                functions.write_todos(todos)
                window["todos"].update(todos)
        case "Edit":
            try:
                todo_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.read_todos()

                index = todos.index(todo_edit)
                todos[index] = new_todo

                functions.write_todos(todos)
                window["todos"].update(todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_complete = values["todos"][0]
                todos = functions.read_todos()
                todos.remove(todo_complete)
                functions.write_todos(todos)
                window["todos"].update(todos)
                window["todo"].update("")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            try:
                window["todo"].update(values["todos"][0])
            except IndexError:
                sg.popup("Please add an item first.", font=("Helvetica", 20))
        case sg.WIN_CLOSED:
            exit()

print("Bye")
window.close()
