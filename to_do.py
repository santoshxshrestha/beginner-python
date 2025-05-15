import csv
from datetime import datetime

file_path = 'tasks.csv'
header = ['Task Name', 'Creation Time']

# Initialize CSV file if not exists
def initialize_csv():
    try:
        with open(file_path, mode='r', newline='') as file:
            pass  # File exists, nothing to do
    except FileNotFoundError:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

initialize_csv()

# Function to read tasks from the CSV file
def read_tasks():
    tasks = []
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            tasks = list(reader)[1:]  # Skip the header row
    except FileNotFoundError:
        print("No tasks file found. Please create a task first.")
    return tasks

# Function to write tasks to the CSV file
def write_tasks(tasks):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write header
        writer.writerows(tasks)  # Write the tasks data

# Function to create a new task
def create_task():
    task_name = input("Enter the task name: ")
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    task_data = [task_name, current_time]
    
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(task_data)
        
    print(f"Task '{task_name}' has been created at {current_time}.")

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks List:")
        for i, row in enumerate(tasks, 1):  # Use 1-based index
            print(f"{i}. Task: {row[0]} | Created at: {row[1]}")

# Function to delete a task
def delete_task():
    tasks = read_tasks()
    if not tasks:
        return  # No tasks to delete
    
    display_tasks(tasks)

    try:
        task_to_delete = int(input("Enter the task number to delete: ")) - 1
        
        if 0 <= task_to_delete < len(tasks):
            tasks.pop(task_to_delete)  # Remove task from list
            write_tasks(tasks)  # Rewrite tasks back to the file
            print(f"Task {task_to_delete + 1} has been removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main program loop
def main():
    print("Welcome to the To-Do List App!")
    while True:
        print("\nYou can select one of the following options:")
        print("-" * 42)
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            create_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            tasks = read_tasks()
            display_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()
