import streamlit as st
import functions

todos = functions.read_todos()


def add_todo():
    todo = st.session_state["add_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("This app is to note down your todos.")


for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()
st.text_input("", placeholder="Add a new todo...",
              on_change=add_todo, key="add_todo")
