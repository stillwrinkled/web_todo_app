import streamlit as st
import functions
from set_working_directory import set_working_directory

set_working_directory()

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)
    print(todo)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity."
         )


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

print("Executed")

st.session_state
