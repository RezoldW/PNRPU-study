import json

tasks = {}

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task():
    description = input("Введите описание задачи: ")
    category = input("Введите категорию задачи: ")
    tasks[description] = {"category": category, "completed": False}

def mark_task_completed():
    description = input("Введите описание задачи: ")
    if description in tasks:
        tasks[description]["completed"] = True
        print("Задача помечена как выполненная")
    else:
        print("Задача не найдена")

def print_tasks_by_category():
    category = input("Введите категорию задачи: ")
    print(f"Задачи в категории '{category}':")
    for description, task in tasks.items():
        if task["category"] == category:
            print(f"Описание: {description}, выполнено: {task['completed']}")

def search_tasks():
    search_query = input("Введите строку для поиска: ")
    found_tasks = []
    for description, task in tasks.items():
        if search_query in description:
            found_tasks.append(description)
    print(f"Результаты поиска для '{search_query}':")
    if found_tasks:
        for task in found_tasks:
            print(task)
    else:
        print("Задачи не найдены")

load_tasks()

while True:
    print("\nМеню:")
    print("1. Добавить задачу")
    print("2. Отметить задачу как выполненную")
    print("3. Вывести задачи в категории")
    print("4. Поиск задачи")
    print("5. Выйти")
    choice = input("Выберите пункт меню: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        mark_task_completed()
    elif choice == "3":
        print_tasks_by_category()
    elif choice == "4":
        search_tasks()
    elif choice == "5":
        save_tasks()
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Попробуйте ещё раз.")