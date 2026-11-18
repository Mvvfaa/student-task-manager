# Student Task Manager

A small, dependency-free Python console application for managing a student's
to-do list.

## Features

- Add tasks with automatically assigned IDs.
- View all tasks and their completion status.
- Mark tasks as completed.
- Delete tasks by ID.
- Validate empty task titles and titles longer than 100 characters.
- Run the application from a terminal or use the `TaskManager` class in Python
  code.

Tasks are kept in memory while the application is running. Closing the
application clears the current task list.

## Requirements

- Python 3.10 or later

No third-party packages are required.

## Setup

1. Clone the repository and change into its directory:

   ```bash
   git clone https://github.com/Mvvfaa/student-task-manager.git
   cd student-task-manager
   ```

2. Verify that Python is available:

   ```bash
   python --version
   ```

   On systems where the Python command is named `python3`, use `python3`
   instead of `python` in the commands below.

## Usage

Start the interactive application with:

```bash
python task_manager.py
```

Choose an option from the menu:

1. Add a task
2. Display tasks
3. Complete a task
4. Delete a task
5. Exit

See the [user guide](docs/userguide.md) for a step-by-step walkthrough and
error-handling tips.

## Testing

Run the complete test suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

The same command is run by the GitHub Actions workflow on pushes and pull
requests targeting `main`.

## Project layout

```text
task_manager.py          Application and TaskManager implementation
tests/test_task_manager.py
                          Unit tests
docs/userguide.md        End-user instructions

```