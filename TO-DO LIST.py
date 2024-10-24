import json

class ToDoList:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                self.todos = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.todos = []

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.todos, file)

    def add_task(self, task):
        self.todos.append({'task': task, 'completed': False})
        self.save()

    def list_tasks(self):
        for index, todo in enumerate(self.todos):
            status = "✓" if todo['completed'] else "✗"
            print(f"{index + 1}. [{status}] {todo['task']}")

    def complete_task(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]['completed'] = True
            self.save()
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.todos):
            del self.todos[index]
            self.save()
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List:")
        todo_list.list_tasks()
        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '3':
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()