# Book Tracker

A web application built with Flask and SQLAlchemy that allows users to track all the books they have read and rate each book.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributing](#contributing)

## Features

- User authentication
- Add books to your reading list
- Rate books you've read
- View your reading history and ratings

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (venv, virtualenv, etc.)
- Flask
- SQLAlchemy

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/book-tracker.git
    cd book-tracker
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the application:**

    ```bash
    flask run
    ```

6. **Access the application:**

    Open your browser and go to `http://127.0.0.1:5000/`

## Usage

1. **Add a book:**

    Go to the "Add Book" page, enter the book's details, and submit.

2. **Rate a book:**

    Navigate to the book in your reading list and submit a rating.

3. **View your reading list:**

    Go to the "My Books" page to see all the books you have added and your ratings.

## Technologies

- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (for development), PostgreSQL/MySQL (for production)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request
