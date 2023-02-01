import streamlit as st
import functions

todos = functions.ReadingTodos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is cool")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Enter a todo here...")