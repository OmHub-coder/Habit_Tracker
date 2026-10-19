# Python Habit_Tracker

A simple command-line Habit Tracker built with Python. This is my first Python project, created to practise programming fundamentals by building a small, practical application.

The application allows users to add habits, mark them as completed, view their daily progress, rename habits, and delete habits. Habit records are stored in a text file so they can be accessed again when the program runs.

## Features

- **Add Habits:** Create new habits to track.
- **Mark Habits as Completed:** Record the date when a habit is completed.
- **View Daily Progress:** See which habits are completed and which are pending for the current day.
- **Rename Habits:** Change the name of an existing habit.
- **Delete Habits:** Remove habits that are no longer needed.
- **File Storage:** Save habit records in a local text file.
- **Input Validation:** Handle invalid menu selections and reject empty habit names.

## Technologies Used

- Python 3
- `datetime` module
- File handling (`open()`, `readlines()`, `writelines()`)
- Object-oriented programming
- Exception handling

## Project Structure

```text
Habit_Tracker/
├── habit_code.py
├── habit_record.txt
├── README.md
├── LICENSE
└── .gitignore
```

`habit_code.py` contains the application code.

`habit_record.txt` stores habit names and completion dates. It is created automatically when you add your first habit, and it is not tracked by Git, so your habits stay on your computer.

`.gitignore` specifies files that should not be tracked by Git.

## Requirements

- Python 3 installed on your computer
- A terminal or code editor, such as VS Code or PyCharm

No external Python packages are required.

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/OmHub-coder/Habit_Tracker.git
```

**2. Open the project folder**

```bash
cd Habit_Tracker
```

**3. Run the application**

```bash
python habit_code.py
```

If your system uses the `py` command on Windows, you can also run:

```bash
py habit_code.py
```

## How It Works

The application displays a menu with six options:

1. Add a habit
2. Mark a habit as completed
3. View today's progress
4. Delete a habit
5. Rename a habit
6. Exit

The user selects an option and interacts with the application through the terminal. Habit names and completion dates are stored in `habit_record.txt`.

Example record format:

```text
Exercise:2026-10-18,2026-10-19
Read books:2026-10-19
```

Each line represents one habit, followed by its recorded completion dates.

## Python Concepts Practised

Building this project helped me practise:

- Classes and objects
- Instance methods
- Conditional statements
- `while` and `for` loops
- User input and type conversion
- Lists and string operations
- File reading and writing
- Exception handling with `try` and `except`
- Working with dates using the `datetime` module

## Current Limitations

This is a beginner-level project, so it has some limitations:

- It uses a plain text file instead of a database.
- It runs in the command line and has no graphical interface.
- It does not provide advanced statistics or habit streak analytics.
- It is designed for simple, local habit tracking.

## What I Learned

This project helped me understand how individual Python concepts can work together to build a usable application. I gained practical experience with file handling, classes, loops, user input, and date-based records.

## Future Improvements

As I continue learning Python, I may improve this project by adding:

- More robust input validation
- Improved date handling and error prevention
- Habit completion statistics
- Automated tests
- Database storage in a future version

## Author

**Om Jindal**

B.Tech CSE student | Learning Python and building projects to strengthen my programming fundamentals.

---

*This is my first Python project and an early step in my programming journey. Feedback and suggestions for improvement are welcome.*
