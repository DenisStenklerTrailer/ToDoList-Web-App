import streamlit as st
import functions

todos = functions.ReadingTodos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.WritingTodos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is cool")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.WritingTodos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Enter a todo here...",
              on_change=add_todo, key="new_todo")

# To je v zelo veliko pomoč ker nam izpisuje podatke
#st.session_state