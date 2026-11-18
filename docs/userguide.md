# Student Task Manager User Guide

## Starting the application

Open a terminal in the project directory and run:

```bash
python task_manager.py
```

If your system uses `python3` for Python 3, run `python3 task_manager.py`
instead.

## Managing tasks

### Add a task

1. Select **1. Add task**.
2. Enter a description, such as `Finish the lab report`.
3. The application confirms the new task ID.

Task titles cannot be empty and cannot exceed 100 characters. Leading and
trailing spaces are removed automatically.

### View tasks

Select **2. Display tasks**. Each task is shown with its ID and status:

- `[ ]` means the task is still open.
- `[x]` means the task is complete.

If no tasks have been added, the application displays `No tasks yet.`

### Complete a task

1. Select **3. Complete task**.
2. Enter the ID of an open task.

The task is marked with `[x]`. A task cannot be completed twice.

### Delete a task

1. Select **4. Delete task**.
2. Enter the task ID to remove.

The application confirms when the task has been deleted. Deleting a task does
not change the IDs of the remaining tasks.

### Exit

Select **5. Exit** to close the application. Tasks are stored only in memory,
so they are not saved after the application closes.

## Handling errors

When an operation fails, read the message displayed after `Error:` and return
to the menu. Common causes include:

- An empty task title.
- A title longer than 100 characters.
- A task ID that does not exist.
- Trying to complete a task that is already complete.

## Running tests

From the repository root, run:

```bash
python -m unittest discover -s tests -v
```

