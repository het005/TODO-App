
task=[]
def add_task(title):
    task.append({"title":title,"compelted":False})

def view_task():
    for index,tasks in enumerate(task):
        status=True
        if tasks['compelted']:
            status="Done"
        else:
            status="Not done"
        print(f"{index+1}:-{tasks['title']}[{status}]")
def complated_Task(index):
    if 0<=index<len(task):
        task[index]["compelted"]=True
def delete_task(index):
    if 0<=index<len(task):
        task.pop(index)


while True:
    print("1.Add Task")
    print("2.View Task")
    print("3.Complete Task")
    print("4.Delete Task")
    print("5.Exit")

    user=input("Enter the option:")

    if user=="1":
        title=input("enter the task")
        add_task(title)
    elif user=="2":
        view_task()
    elif user=="3":
        view_task()
        idx=int(input("Enter task number to complete:"))-1
        complated_Task(idx)
    elif user=="4":
        view_task()
        idx=int(input("Enter task number to delete"))-1
        delete_task(idx)
        print("Task Deleted successfully")
    elif user=="5":
        break
    else:
        print("Invalid Choise")
