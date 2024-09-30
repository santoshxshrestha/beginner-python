tasks=[]
def addTask():
    task=input("please enter a task:")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

    
def listTask():
    if not tasks:
        print('there are no task currently.')
    else:
        print('current tasks: ')
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")


def deleteTask():
    listTask()
    try:
        taskToDelete = int(input('enter the # to delete: '))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")

        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("invalid input.")
if __name__=="__main__":
    print("welcome to the to do list app")
    while True:
        print("\n")
        print("You can select one of the folling options.")
        print("-"*42)
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        break

while True:
        choice = input("enter your choice: ")

        if (choice=="1"):
            addTask()

        elif (choice=="2"):
            deleteTask()

        elif (choice=="3"):
            listTask()
        elif (choice=="4"):
            break
        else:
            print("invalid input, please try again")

print("Good bye")