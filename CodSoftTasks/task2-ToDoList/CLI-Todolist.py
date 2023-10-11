import os
from datetime import datetime

# Define the path to the Todo list file
TODO_FILE = "todo.txt"

# Check if the Todo file exists, and create it if not
if not os.path.exists(TODO_FILE):
    with open(TODO_FILE, "w") as file:
        pass

def display_todos():
    with open(TODO_FILE, "r") as file:
        todos = file.readlines()
        if not todos:
            print("No todos found. You're all caught up!")
        else:
            print("Todo List:")
            for i, todo in enumerate(todos, start=1):
                parts = todo.strip().split(" ", 3)
                if len(parts) == 4:
                    date, priority, task, status = parts
                    print(f"{i}. Date: {date}, Priority: {priority}, Task: {task}, Status: {status}")
                else:
                    print(f"{i}. Invalid Todo Format: {todo.strip()}")


# def add_todo(priority, task):
#     current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open(TODO_FILE, "a") as file:
#         file.write(f"{current_date} {priority} {task} Incomplete\n")
#     print(f"Added: Date: {current_date}, Priority: {priority}, Task: {task}")
def add_todo(priority, task):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TODO_FILE, "a") as file:
        file.write(f"{current_date} Priority: {priority}, Task: {task}, Status: Incomplete\n")
    print(f"Added: Date: {current_date}, Priority: {priority}, Task: {task}")

# Rest of the code remains the same...

def update_todo(index, completed):
    try:
        with open(TODO_FILE, "r") as file:
            todos = file.readlines()
        if 1 <= index <= len(todos):
            parts = todos[index - 1].strip().split(" ", 3)
            if len(parts) == 4:
                date, priority, task, _ = parts
                with open(TODO_FILE, "w") as file:
                    for i, todo in enumerate(todos):
                        if i == index - 1:
                            file.write(f"{date} {priority} {task} {completed}\n")
                        else:
                            file.write(todo)
                print(f"Updated: Task {index} - Completed: {completed}")
            else:
                print(f"Invalid Todo Format: {todos[index - 1].strip()}")
        else:
            print("Invalid index. Todo not updated.")
    except FileNotFoundError:
        print("Todo file not found. Create a todo list first.")

def remove_todo(index):
    try:
        with open(TODO_FILE, "r") as file:
            todos = file.readlines()
        if 1 <= index <= len(todos):
            removed_todo = todos.pop(index - 1)
            with open(TODO_FILE, "w") as file:
                file.writelines(todos)
            print(f"Removed: {removed_todo.strip()}")
        else:
            print("Invalid index. Todo not removed.")
    except FileNotFoundError:
        print("Todo file not found. Create a todo list first.")

def main():
    while True:
        print("\nOptions:")
        print("1. Display Todo List")
        print("2. Add a Todo")
        print("3. Update a Todo")
        print("4. Remove a Todo")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_todos()
        elif choice == "2":
            priority = input("Enter priority (e.g., High, Medium, Low): ")
            task = input("Enter a new todo: ")
            add_todo(priority, task)
        elif choice == "3":
            index = int(input("Enter the index of the todo to update: "))
            completed = input("Is the task completed? (Yes/No): ").capitalize()
            if completed in ["Yes", "No"]:
                update_todo(index, completed)
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")
        elif choice == "4":
            index = int(input("Enter the index of the todo to remove: "))
            remove_todo(index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
