import os

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
                parts = todo.strip().split(" ", 1)
                if len(parts) == 2:
                    priority, task = parts
                    print(f"{i}. Priority: {priority}, Task: {task}")
                else:
                    print(f"{i}. Invalid Todo Format: {todo.strip()}")


def add_todo(priority, task):
    with open(TODO_FILE, "a") as file:
        file.write(f"{priority} {task}\n")
    print(f"Added: Priority: {priority}, Task: {task}")

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
        print("3. Remove a Todo")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_todos()
        elif choice == "2":
            priority = input("Enter priority (e.g., High, Medium, Low): ")
            task = input("Enter a new todo: ")
            add_todo(priority, task)
        elif choice == "3":
            index = int(input("Enter the index of the todo to remove: "))
            remove_todo(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
