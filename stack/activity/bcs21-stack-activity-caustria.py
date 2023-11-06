class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        self.next = None

class TaskManager:
    def __init__(self):
        self.head = None

    def add_task(self, title, description):
        new_task = Task(title, description)
        new_task.next = self.head
        self.head = new_task
        print(f'Task "{title}" added.')

    def mark_completed(self, title):
        current = self.head
        while current:
            if current.title == title:
                current.completed = True
                print(f'Task "{title}" marked as completed.')
                return
            current = current.next
        print(f'Task "{title}" not found.')

    def display_tasks(self):
        if not self.head:
            print('No tasks to display.')
        else:
            print('Tasks:')
            current = self.head
            task_number = 1
            while current:
                status = 'Completed' if current.completed else 'Not Completed'
                print(f'{task_number}. Task Name: {current.title}, Description: {current.description}, Status: {status}')
                current = current.next
                task_number += 1

    def run(self):
        while True:
            print('\nTask Manager Menu:')
            print('1. Add Task')
            print('2. Mark Task as Completed')
            print('3. Display Tasks')
            print('4. Exit')
            choice = input('Enter the number of your choice (1/2/3/4): ')

            if choice == '1':
                title = input('Enter task title: ')
                description = input('Enter task description: ')
                self.add_task(title, description)
            elif choice == '2':
                title = input('Enter the task title to mark as completed: ')
                self.mark_completed(title)
            elif choice == '3':
                self.display_tasks()
            elif choice == '4':
                break
            else:
                print('Invalid choice. Please choose a valid number.')

if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.run()

