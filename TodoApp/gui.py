import filefunc
import FreeSimpleGUI as sg

input_label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter to-do here")
check_box = sg.DropDown(size=10, values=[1,2,3])

window = sg.Window('My To-Do App', layout=[[input_label, input_box], [check_box]])
window.read() # window open and prompt waiting for user action
window.close()