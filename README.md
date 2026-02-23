SongVault

Artist Operations Dashboard built with Flask, MySQL, and Docker.

SongVault is a containerized web application designed to manage a music catalogue, release tracking, and publishing workflow in a structured and reproducible environment. It demonstrates backend development, database modeling, and multi-container orchestration using Docker Compose.

Features

Create, edit, delete, and search songs (full CRUD workflow)

Song status tracking (Draft / Registered / Released)

Dashboard summary with real-time counts

Persistent MySQL database (Docker volume-backed)

Production-style Gunicorn server

Fully containerized environment using Docker Compose

Tech Stack

Python 3.12

Flask

Flask-SQLAlchemy

MySQL 8

PyMySQL

Gunicorn

Docker

Docker Compose

Architecture Overview

SongVault runs as a two-service Docker Compose stack:

web → Flask application served via Gunicorn

db → MySQL 8 database container

The application uses SQLAlchemy as the ORM layer and connects via environment variables for secure configuration.

Getting Started
1. Clone the repository
git clone https://github.com/yourusername/songvault.git
cd songvault
2. Create a .env file

Example:

MYSQL_DATABASE=songvault
MYSQL_USER=songvault_user
MYSQL_PASSWORD=songvault_pass
MYSQL_ROOT_PASSWORD=root_pass_change_me
SECRET_KEY=change_me
3. Build and start the application
docker compose up --build
4. Open in browser
http://localhost:8080
Stopping the Application

Stop containers:

docker compose down

Reset database (deletes stored data):

docker compose down -v
Why This Project Exists

SongVault was built as a practical demonstration of:

Designing relational database schemas

Implementing CRUD workflows in Flask

Containerizing applications for reproducible environments

Managing multi-service stacks with Docker Compose

It reflects a real-world backend workflow rather than a tutorial-based toy example.
