import streamlit as st
import filefunc

def add_todo():
    todo_item = st.session_state["new_todo"]
    todo_item = todo_item.title() + '\n'
    todos.append(todo_item)
    filefunc.write_todos(todos)
    st.session_state["new_todo"] = ''


todos = filefunc.get_todos()
st.title("My Todo web app")
st.subheader("This is sub header")
st.write("Below is loaded from file")

for item, todo in enumerate(todos):
    checked_todos = st.checkbox(todo, key=todo)
    if checked_todos:
        todos.pop(item)
        filefunc.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Type in todo", placeholder='Add todo here', on_change=add_todo, key='new_todo')
# st.session_state
