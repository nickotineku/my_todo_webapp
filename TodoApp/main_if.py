# from filefunc import get_todos, write_todos
import filefunc
import time
"""
This is multi-line string
"""

"this is\
single line string\
with multiple line in code editor"

now = time.strftime('%a %d-%b-%Y  %H:%M')
print("The below here is current data and time")
print(f'It is {now} ')

while True:
    user_action = input("Please type add/show/edit/complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        # read all list in file
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = filefunc.get_todos()
        todos.append(todo + '\n')

        filefunc.write_todos(todos)

        # write new list into file
        # file = open('todos.txt', 'w')
        # todos.append (todo+'\n')
        # file.writelines(todos)
        # file.close()

    elif user_action.startswith('show'):
        # read all list in file
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = filefunc.get_todos()

        # new_todos = [item.strip('\n') for item in todos] --> list comprehension to remove '\n'
        # enumerate adds a counter to an iterable and returns it as an enumerate object.
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item.title()}")
    elif user_action.startswith('edit'):
        try:
            # recall todo list in the file
            todos = filefunc.get_todos()

            todo_selected = user_action[5:]
            todo_index = int(todo_selected) - 1  # convert to int since input return string type
            todo_to_update = todos[todo_index].strip('\n')
            print(f"The '{todo_to_update}' will be edited")
            todo_update = input("Please type new todo : ")
            todos[todo_index] = todo_update + '\n'

            # write edited todos list into file
            filefunc.write_todos(todos)

        except ValueError:
            print(f"You input '{user_action}' which is wrong command, please put item number")
            continue

    elif user_action.startswith('complete'):
        try:
            number = user_action[9:]
            number = int(number)

            todos = filefunc.get_todos()

            remove_item = todos.pop(number-1).strip('\n')

            filefunc.write_todos(todos)

            print(f"The {remove_item} successfully removed from the list")
        except IndexError:
            todos = filefunc.get_todos()
            print(f'There are only {len(todos)} items in the list')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command, please try again")
