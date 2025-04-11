# ✅ Simple Python To-Do List

A beginner-friendly, menu-driven to-do list app built with Python. This project runs in the terminal and lets users add, view, and delete tasks easily.

---

## 📋 Features

- 📌 Add new tasks
- 👀 View all current tasks
- ❌ Delete tasks by their number
- 🔐 Input validation to prevent crashes
- 🧼 Clean and readable menu-based interface

---

## 🚀 Getting Started

### Requirements

- Python 3.x installed on your system

### Running the App

1. Clone the repository or download the Python file:

```bash
git clone https://github.com/your-username/todo-list-python.git
cd todo-list-python
Run the script:

bash
Copy
Edit
python todo.py
🖥️ How It Works
When you run the program, you'll see a simple menu like this:

=== TO-DO LIST MENU ===
1. Add a task
2. View tasks
3. Delete a task
4. Quit
You can type the number to choose what you'd like to do. The app will guide you through the process and provide helpful feedback.

🛠 Code Structure
show_menu() — Displays the main menu

add_task(tasks) — Adds a non-empty task to the list

view_tasks(tasks) — Shows current tasks with numbered list

delete_task(tasks) — Deletes a task by its number with input checks

main() — Runs the app loop, manages user input

💡 Future Improvements
Save tasks to a text or JSON file for persistence

Add "Mark as complete" feature

Support due dates or priorities

Build a GUI with Tkinter or a web version with Flask
