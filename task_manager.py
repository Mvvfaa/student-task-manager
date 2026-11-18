"""Student Task Manager - a simple console application."""


class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed


class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        task = Task(self._next_id, title)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def complete_task(self, task_id):
        raise NotImplementedError

    def delete_task(self, task_id):
        raise NotImplementedError