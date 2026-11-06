# Python API, SQL & Testing Assignment

A practical Python assignment demonstrating API integration, database management using SQL, and automated testing with Pytest.

## Project Overview

This repository contains three independent tasks completed using Python and SQLite.

### Task 1: GitHub REST API

- Fetches public information for three GitHub users.
- Displays each user's login and public repository count.
- Verifies HTTP status code `200` before processing API responses.
- Uses the Python `requests` library.

**File:** `task1_api/github_api.py`

### Task 2: SQL Library Database

- Creates a SQLite database named `library`.
- Creates a `books` table with ID, title, author, year, and price.
- Inserts eight book records.
- Retrieves books priced above 500.
- Sorts books by price in descending order.
- Counts total books.
- Updates a book's price using the `WHERE` clause.

**Files:**
- `task2_sql/library.py`
- `task2_sql/library.sql`

### Task 3: Pytest Unit Testing

- Implements an `is_adult(age)` function.
- Returns `True` for ages 18 and above.
- Returns `False` for ages below 18.
- Raises `ValueError` for negative ages.
- Includes three test cases using Pytest.

**Files:**
- `task3_pytest/age.py`
- `task3_pytest/test_age.py`

## Technologies Used

- Python
- GitHub REST API
- Requests
- SQLite
- SQL
- Pytest
- Git & GitHub

## Project Structure

```text
python-api-sql-testing-assignment/
│
├── task1_api/
│   └── github_api.py
│
├── task2_sql/
│   ├── library.py
│   └── library.sql
│
├── task3_pytest/
│   ├── age.py
│   └── test_age.py
│
├── README.md
└── .gitignore
```

## Installation & Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-api-sql-testing-assignment.git
```

Navigate to the project:

```bash
cd python-api-sql-testing-assignment
```

Install dependencies:

```bash
py -m pip install requests pytest
```

## How to Run

**Task 1 – GitHub API**

```bash
cd task1_api
py github_api.py
```

**Task 2 – SQL Library Database**

```bash
cd task2_sql
py library.py
```

**Task 3 – Pytest**

```bash
cd task3_pytest
py -m pytest -v
```

## Testing

Run the following command to execute the test suite:

```bash
py -m pytest -v
```

Expected result: 3 tests passed.

## Author

**Humna Malik**

Software Engineering | Python | API | SQL | Software Testing

---

This repository was created as part of a practical programming assignment.