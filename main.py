class Task:

    # Инициализация задачи
    def __init__(self, description, deadline):
        self.description = description # описание задачи
        self.deadline = deadline # срок выполнения задачи
        self.completed = False  # По умолчанию задача не выполнена

    # Отмечает задачу как выполненную
    def mark_as_completed(self):
        self.completed = True

    # Возвращает строковое представление задачи
    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"[{status}] {self.description} (до {self.deadline})"

# Инициализация менеджера задач
class TaskManager:
    def __init__(self):
        self.tasks = []

# Добавление новой задачи
    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

# Отметка задачи как выполненной
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Задача с таким индексом не найдена.")

# Вывод списка невыполненных задач
    def show_pending_tasks(self):
        print("Текущие задачи:")
        for idx, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{idx}: {task}")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавляем задачи
    manager.add_task("Сходить в магазин", "2024-12-05")
    manager.add_task("Закончить проект", "2024-12-10")
    manager.add_task("Позвонить маме", "2024-12-03")

    # Показываем текущие задачи
    manager.show_pending_tasks()

    # Завершаем одну из задач
    manager.complete_task(1)

    # Показываем оставшиеся задачи
    manager.show_pending_tasks()
