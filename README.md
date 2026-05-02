# goit-pycore-hw-04

Simple Python homework project with four tasks for working with files,
directories, and a small command-line assistant bot.

## Project files

- `task01.py` - calculates total and average salary from `salary_file.txt`.
- `task02.py` - reads cat information from `cats_file.txt`.
- `task03.py` - prints a colored folder structure for a selected directory.
- `task04.py` - runs a simple contact assistant bot.
- `salary_file.txt` - source data for task 1.
- `cats_file.txt` - source data for task 2.
- `requirements.txt` - project dependencies.

## Setup

Use a virtual environment before running the scripts. The project depends on
packages from `requirements.txt`, especially `colorama` for colored terminal
output in tasks 3 and 4.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run tasks

```bash
python task01.py
python task02.py
python task03.py
python task03.py /path/to/folder
python task04.py
```

## Assistant bot commands

When running `task04.py`, use these commands:

```text
hello
add <name> <phone>
change <name> <phone>
phone <name>
all
close
exit
```
