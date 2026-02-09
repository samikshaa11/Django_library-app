# Django_library-app

A simple Django-based web application to manage books in a library. Users can view a list of books, add new books, and keep track of authors and publication dates.

Features:

- View all books in the library with details (title, author, published date).

- Add, edit, and delete books (if admin functionality added).

- Responsive table with Bootstrap styling.

- Easy to extend for borrowing, users, and other library functionalities.

Tech Stack:

Backend: Django 6.0

Frontend: HTML, Bootstrap 5, CSS

Database: SQLite (default, can be replaced with PostgreSQL/MySQL)

Python version: 3.14

Other libraries: (e.g., if you use Django REST framework, list here)

Installation:

Clone the repository:

git clone https://github.com/samikshaa11/Django_library-app.git
cd library-app

Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Open the app in your browser:

http://127.0.0.1:8000/library_books/

Project Structure
library_project/
├─ library_books/ # Django app for managing books
│ ├─ models.py # Book model
│ ├─ views.py # Views to list books
│ ├─ templates/
│ │ └─ library_books/
│ │ └─ book_list.html # Book list template
│ │ └─ book_details.html
│ │ └─ style.css
| ├─ templates/
│ └─ base_generic.html # Base template for layout
├─ library_project/ # Project settings
│ └─ settings.py
│ └─ urls.py
│ └─ asgi.py
├─ db.sqlite3 # Database
├─ manage.py
└─ requirements.txt

Usage

Navigate to /library_books/ to see all books.

Use the Django admin panel (/admin/) to add or edit books if admin access is set up.

Contributing

Fork the repository

Create a new branch (git checkout -b feature/YourFeature)

Make your changes

Commit (git commit -m "Add some feature")

Push (git push origin feature/YourFeature)

Create a Pull Request
