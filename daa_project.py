'''class Queue:
    def __init__(self):
        # Initialize an empty list to hold tasks
        self.tasks = []

    def enqueue(self, task):
        # Add a task to the end of the queue
        self.tasks.append(task)
        print(f"Task added: {task}")

    def dequeue(self):
        # Remove and return the task at the front of the queue
        if not self.is_empty():
            return self.tasks.pop(0)
        else:
            return "No tasks to remove."

    def view(self):
        # Return the list of tasks or a message if empty
        return self.tasks if self.tasks else "No tasks available."

    def is_empty(self):
        # Check if the queue is empty
        return len(self.tasks) == 0

def main():
    queue = Queue()  # Create a Queue instance

    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task details: ")
            queue.enqueue(task)  # Add the task to the queue
        elif choice == '2':
            removed_task = queue.dequeue()  # Remove the first task
            print(removed_task)  # Show the removed task
        elif choice == '3':
            tasks = queue.view()  # Get the current tasks
            print("Current Tasks:", tasks)  # Display tasks
        elif choice == '4':
            print("Exiting...")  # Exit the program
            break
        else:
            print("Invalid choice, please try again.")  # Handle invalid input

if __name__ == "_main_":
    main()  # Start the program'''

class Queue:
    def __init__(self):
        self.tasks = []

    def enqueue(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def dequeue(self):
        if not self.is_empty():
            return self.tasks.pop(0)
        else:
            return "No tasks to remove."

    def view(self):
        return self.tasks if self.tasks else "No tasks available."

    def is_empty(self):
        return len(self.tasks) == 0

def main():
    queue = Queue()  
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task details: ")
            queue.enqueue(task)  
        elif choice == '2':
            removed_task = queue.dequeue()  
            print(removed_task)  
        elif choice == '3':
            tasks = queue.view()  
            print("Current Tasks:", tasks)  
        elif choice == '4':
            print("Exiting...")  
            break
        else:
            print("Invalid choice, please try again.") 

if __name__ == "__main__":
    main()  