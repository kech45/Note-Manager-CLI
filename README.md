# Note-Manager-CLI

A simple CLI note-taking application built in Python.
Allows adding, listing, viewing and deletion of notes from the terminal.

## Installation

1. Cloning the repository:
```bash
git clone https://github.com/kech45/Note-Manager-CLI.git
```

2. Creating a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the package
```bash
pip install -e .
```

The 'pyproject.toml' file creates the notes CLI command,
and using 'pip install -e .' lets changes work instantly without reinstalling.

## Usage

### Add a note
```bash
notes add "Meeting with client" "Discuss Q3 budget and timeline"
```

### List all notes
```bash
notes list
```

### Show a note by given ID
```bash
notes show 1
```

### Delete a note by given ID
```bash
notes delete 1
```

### Help
```bash
notes --help
```

## Persistence

**SQLite** - chosen for local persistence without external dependencies. 
Python's built-in `sqlite3` module handles everything needed.

## Code structure
The project is split into three layers:
- **CLI layer** (`cli.py`) - handles user input and output only
- **Business logic layer** (`manager.py`) - handles validation and logic
- **Storage layer** (`storage.py`) - handles all database operations

## Testing

### Running unit-tests
```bash
python -m unittest discover
```

### Install required tools
```bash
pip install requirements.txt
```

### Running flake8 linter
```bash
flake8 --max-line-length 88 notes/ tests/
```

### Running black code formatter
```bash
black --check notes/ tests/
```

## Branching Strategy 

- `main` - production-ready, stable code  
- `dev` - integration branch for ongoing development  
- `feature/*` - used to develop new features  

Each feature is developed in isolation and afterwards merged using Pull Requests.

## CI

This project uses `GitHub Actions` for continuous integration.
On every push and pull request the pipeline automatically runs the following:
    - All unit tests
    - Code style checking with black
    - Linting with flake8