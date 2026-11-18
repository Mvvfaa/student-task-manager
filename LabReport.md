# Lab Report: Student Task Manager

**Name:** YOUR NAME
**Reg. No:** YOUR REG NO
**Course:** CSC418 - DevOps for Cloud Computing
**Repository:** https://github.com/Mvvfaa/student-task-manager

---

## 1. Git vs GitHub; add, commit and push

Git is a version control tool that runs on my computer and tracks changes to files. GitHub is an online platform that hosts Git repositories and adds collaboration features like Issues, Pull Requests and Actions.

- **git add:** moves changed files to the staging area, ready to be saved.
- **git commit:** saves the staged changes as a snapshot in the local history, with a message.
- **git push:** uploads local commits to the remote repository on GitHub.

## 2. Branches, Pull Requests and merge conflicts

Branches let me build a feature separately, so unfinished work does not break `main`. Pull Requests let others review the changes and discuss them before they are merged.

A merge conflict happens when two branches change the same lines of a file differently, and Git cannot decide which version to keep.

## 3. Fetch vs pull; merge vs rebase

- **fetch** downloads new commits from the remote without changing my working files. **pull** is fetch followed by a merge into the current branch.
- **merge** joins two branches and keeps both histories, usually with a merge commit. **rebase** moves my commits on top of another branch, which gives a straight, linear history.

## 4. GitHub Issues and Actions

Issues track features, bugs and documentation tasks, so the team knows what needs doing and who is working on it. GitHub Actions runs the tests automatically on every push and pull request, so errors are caught before the code is merged.

## 5. Difficulty faced and solution

When I opened the pull request for `feature/delete-task`, GitHub reported a merge conflict in `task_manager.py`, because `main` had already received the changes from `feature/add-task`. I opened the conflict editor, saw that the two sides contained different work (my `delete_task` method and the `add_task` validation), and chose "Accept both changes" so nothing was lost. I then removed the conflict markers, marked the file as resolved, committed the merge and ran the app to confirm it worked.