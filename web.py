import streamlit as st
import functions
from set_working_directory import set_working_directory

set_working_directory()


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity."
         )
todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add new todo...")

print("Executed")