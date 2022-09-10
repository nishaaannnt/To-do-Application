import tkinter
import tkinter.messagebox
import pickle
from turtle import bgcolor


# this step is necessary
root=tkinter.Tk()

root.geometry("320x370")
root.config(bg="#26242f")
root.resizable(0,0)
# to add title to your GUI
root.title("To-Do List")

# CREATING THE GUI

def add_task():
    # get the task which is entered
    task=entry_tasks.get()
    # if no task is entered
    if task!="":
        listbox_tasks.insert(tkinter.END,task)
        entry_tasks.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="Please Enter a Task ")

#deleting a task
def delete_task():
    try:
        #to get current task which is selected
        # 0 is to specify that only one task is selected
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    # if no task is selected then throw this error
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="Please Select a Task ")

def save_tasks():
    # get the tasks entered in the listbox
    tasks=listbox_tasks.get(0,listbox_tasks.size())
    # adding the tasks in the file to be saved
    pickle.dump(tasks,open("tasks.dat","wb"))

def load_tasks():
    try:
        # getting tghe tasks from tasks.dat
        tasks=pickle.load(open("tasks.dat","rb"))
        # deleting the tasks in listbox to avoid confusion
        listbox_tasks.delete(0,tkinter.END)
        # getting the taaks of dat file
        for i in tasks:
            listbox_tasks.insert(tkinter.END,i)
        
    # if no tasks are saved in dat file
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="Task.dat is not present ")



#creating a frame to store listbox_tasks and scroll bar in it
frame_root=tkinter.Frame(root)
frame_root.pack()

listbox_tasks=tkinter.Listbox(frame_root,height=15,width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scroll_tasks=tkinter.Scrollbar(frame_root)
scroll_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y )

# adding scrollbar functionality
listbox_tasks.config(yscrollcommand=scroll_tasks.set,bg="#26242f",fg="white")
scroll_tasks.config(command=listbox_tasks.yview)

entry_tasks=tkinter.Entry(root,width=57)
entry_tasks.pack()

button_add_tasks=tkinter.Button(text="Add",width=48,command=add_task,bg="#26242f",fg="white")
button_add_tasks.pack()

button_delete_tasks=tkinter.Button(text="Delete",width=48,command=delete_task,bg="#26242f",fg="white")
button_delete_tasks.pack()

button_load_tasks=tkinter.Button(text="Load",width=48,command=load_tasks,bg="#26242f",fg="white")
button_load_tasks.pack()

button_save_tasks=tkinter.Button(text="Save",width=48,command=save_tasks,bg="#26242f",fg="white")
button_save_tasks.pack()


# the below is important to make your gui visible constantly
root.mainloop()