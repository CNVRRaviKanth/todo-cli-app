tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(index):
    tasks.pop(index)   # ❌ Bug: index should be index-1

if __name__ == "__main__":
    show_tasks()
