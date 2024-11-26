# **Database GUI Project**

## **Introduction**

This project creates a simple database GUI that performs CRUD (Create, Read, Update, Delete) operations. The application allows users to interact with a database of courses, including adding, editing, and deleting courses.

### Live Web App - https://database-gui-ho63.onrender.com

## **Features**

- Create new courses
- Read existing courses
- Update existing courses
- Delete existing courses
- User-friendly GUI interface

## **Technologies Used**

- Front-end: HTML, CSS
- Framework: Flask
- Database: postgreSQL

## **Installation**

### Dependencies

- Install postgreSQL from the official website
- Install Flask dependencies using pip:

```bash
pip install -r requirements.txt
```

## **Running the Application**

1. Run `app.py` to start the Flask application
2. Open a web browser and navigate to `http://localhost:5000`

## **Database Schema**

The database schema consists of a single table, `courses`, with the following columns:

- `id` (primary key)
- `name`
- `fees`
- `duration`

## **API Endpoints**

- `/`: Home page
- `/create`: Create new course
- `/edit`: Edit existing course
- `/delete`: Delete existing course

## **License**

This project is licensed under the open source MIT License.
