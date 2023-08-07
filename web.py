import streamlit as st
import functions
st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("This app is to note down your todos.")

todos = functions.read_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input("", placeholder="Add a new todo...")
