# flask-assignment1

The following is the reference solution for Option A. The structure and all sections remain the same for Option B — only the project description, endpoint table, and version history content change.

# Flask Voting Application

## Description

A lightweight web application built with Python and Flask that allows users to cast
votes for candidates through URL-based requests and view live results. Built to
demonstrate REST API development and Git versioning workflows.

---

## Installation and Setup

Prerequisites

- Python 3.x installed on your machine
- pip (Python package manager)
- Git

Steps

    # Clone the repository
    git clone https://github.com/YOUR_USERNAME/flask-assignment.git

    # Navigate into the project folder
    cd flask-assignment

    # Install the required dependency
    pip install flask

    # Run the application
    python app.py

The application will start on http://localhost:5000

---

## API Endpoints

| Endpoint      | Method | Description                              | Example Response                    |
|---------------|--------|------------------------------------------|-------------------------------------|
| /             | GET    | Home page                                | Welcome to the Voting App           |
| /health       | GET    | Confirms the app is running              | App is running                      |
| /vote/<name>  | GET    | Casts one vote for the given name        | Vote recorded for Alice. Total: 2   |
| /results      | GET    | Returns all current vote counts as JSON  | {"Alice": 2, "Bob": 1}              |
| /reset        | GET    | Clears all votes                         | All votes have been reset           |

---

## Git Workflow

All development was done in the dev branch. Once a feature was complete and tested,
dev was merged into main to create a new stable release. No code was committed
directly to main at any point.

    dev   ---●-----------●---
              |           |
    main  ----●-----------●---
             v1.0        v2.0

---

## Version History

| Version   | What Was Included                                          |
|-----------|------------------------------------------------------------|
| Version 1 | Basic Flask app with / and /health endpoints               |
| Version 2 | Added /vote, /results, and /reset endpoints                |

---

## Screenshots

### Application Running
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/0221441c-0a0a-4be4-84cd-11a723992f32" />
<img width="2532" height="900" alt="image" src="https://github.com/user-attachments/assets/72e43935-5c2d-4c8c-a59a-8a7f6769f0d8" />
<img width="2566" height="918" alt="image" src="https://github.com/user-attachments/assets/d33c615f-853e-4cb8-aa4d-eac58fba67ea" />
<img width="2940" height="1594" alt="image" src="https://github.com/user-attachments/assets/a9075055-d393-45ed-8fd8-20679d8fa074" />
<img width="2934" height="1608" alt="image" src="https://github.com/user-attachments/assets/3650d3ce-ed1a-4492-a619-18d8427cdf30" />



### Branch Structure on GitHub
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/62336cb3-1aee-4181-a181-4d321803918c" />


### Commit and Merge History
<img width="2694" height="746" alt="image" src="https://github.com/user-attachments/assets/51f1c7e0-ae01-4908-aa19-872ae43bf8d6" />



Final repository structure:
flask-assignment/
├── app.py
├── README.md
└── screenshots/
    ├── app_running.png
    ├── branches.png
    └── merge_history.png
