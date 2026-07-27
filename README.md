# EduSchema

Terminal-based course management system for an education provider — courses, instructors, student enrolment, and assessments, backed by MySQL.

> ### ⚠️ Hardcoded database password
>
> [`db_connection.py`](db_connection.py) contains a MySQL password in plain text, and this repository is public. See [Configuration](#configuration) for how to move it to an environment variable.

## Overview

A menu-driven CLI covering the four things a small course provider needs to track: what courses exist, who teaches them, who is enrolled, and how those students are doing.

Each domain is a separate module with its own operations, wired together by a nested menu in `main.py`. All state lives in a MySQL database — the Python side holds nothing between runs.

## Features

### Course management
- Add, update, and remove courses (name, description, duration in weeks, level)
- Search courses
- Sort courses

### Instructor management
- Add, update, and remove instructors
- Assign instructors to courses

### Student enrolment
- Register students
- Enrol students on courses
- Update student progress

### Assessment and grades
- Create assessments
- Enter grades
- View grades

## Tech Stack

Python 3 · MySQL via `mysql-connector-python`

## Prerequisites

- Python 3.8+
- A running MySQL server
- A database named `EduSchema`

## Installation

```bash
git clone https://github.com/Namans12/EduSchema.git
cd EduSchema
pip install mysql-connector-python
```

Create the database:

```sql
CREATE DATABASE EduSchema;
```

The repository does not include a schema file — tables are expected to already exist. Their structure can be inferred from the queries in each module (`course_management.py`, `instructor_management.py`, `student_enrollment.py`, `assessment_and_grades.py`).

## Configuration

Connection settings live in [`db_connection.py`](db_connection.py):

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="...",        # hardcoded
    database="EduSchema",
)
```

**The password is committed in plain text.** Recommended fix:

```python
import os
import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host=os.environ.get("EDUSCHEMA_HOST", "localhost"),
        user=os.environ.get("EDUSCHEMA_USER", "root"),
        password=os.environ["EDUSCHEMA_PASSWORD"],
        database=os.environ.get("EDUSCHEMA_DB", "EduSchema"),
    )
```

Then set `EDUSCHEMA_PASSWORD` in your environment. Note that rewriting the file does not remove the value from git history — if that password is used anywhere else, change it there too.

## Usage

```bash
python main.py
```

You get a top-level menu:

```
Welcome to EduSchema
1. Course Management
2. Instructor Management
3. Student Enrollment
4. Assessment and Grades
5. Exit
```

Each option opens a submenu of operations, prompting for the fields it needs.

## Project Structure

```
main.py                     entry point, nested menu loop
db_connection.py            MySQL connection factory
course_management.py        add / update / remove / search / sort courses
instructor_management.py    add / update / remove / assign instructors
student_enrollment.py       register, enrol, update progress
assessment_and_grades.py    create assessments, enter and view grades
```

## Limitations

- No schema migration or setup script — tables must be created by hand
- No input validation beyond Python's own type coercion; a non-numeric answer to a numeric prompt raises
- No authentication or roles — anyone running the script has full access
- Single-user, synchronous, terminal-only

## Related Repositories

| Repo | Relationship |
|---|---|
| [`TIMS`](https://github.com/Namans12/TIMS) | Similar shape — Python + MySQL inventory system with a web front end |
