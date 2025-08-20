import filefunc
import FreeSimpleGUI as sg


input_label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter to-do here", key='todo')
check_box = sg.DropDown(size=10, values=[1,2,3])
add_button = sg.Button("Add")

list_box = sg.Listbox(values=filefunc.get_todos(), key='todos_list',
                      enable_events=True, size=[45, 10])# Enable_events used for trigger event when select the list
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[input_label, input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica, 20'))
while True:
    event, value = window.read()  # window open and prompt waiting for user action # Return tuple
    # print(event)
    # print(value)
    match event:
        case "Add":
            todos = filefunc.get_todos()
            new_todo = value['todo'].title() + '\n'
            todos.append(new_todo)
            filefunc.write_todos(todos)
            new_todo = new_todo.strip("\n")
            print(f"{new_todo} already added into file")
            window['todos_list'].update(todos)
        case "Edit":
            todos = filefunc.get_todos()
            if value["todos_list"]:
                selected_todo = value["todos_list"][0]  # selected todo to edit in the listbox
                index_todo = todos.index(selected_todo)  # get index of selected todo from todos list in the file
            else:
                window['todo'].update(value='Please select todo in the list before click edit!!')
                continue
            if value['todo'] != "":  # check if value in "type in todo" field is empty or not
                new_todo = value['todo'].title() + '\n'  # get text value from input box
                todos[index_todo] = new_todo  # assign text value in selected index
                filefunc.write_todos(todos)
                window['todos_list'].update(values=todos)  # execute list box update from todos list
            else:
                continue
        case "Complete":
            todos = filefunc.get_todos()
            if value["todos_list"]:
                todo_to_complete = value["todos_list"][0]
                todos.remove(todo_to_complete)
                filefunc.write_todos(todos)
                window['todos_list'].update(values=todos)
            else:
                window['todo'].update(value='Please select todo in the list before click edit!!', text_color="red")
                continue
        case "todos_list":
            window['todo'].update(value=value['todos_list'][0])  # get update selected todo into text box
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
