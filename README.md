# SecureAuth Python 🔐

A full-stack authentication system built with Python, FastAPI, and Kivy, developed as a personal learning project to explore backend architecture, authentication systems, and secure software design.


[![Kivy](https://img.shields.io/badge/Kivy-UI-1da6e0?logo=c)](https://kivy.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)](https://sqlite.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE)


Python • FastAPI • Kivy • SQLite • MIT License • Educational Project

## 🚀 Features

Desktop client built with KivyMD
REST API backend
User registration and secure login
Password hashing with bcrypt
Password strength validation
Duplicate username/email prevention
Brute-force protection with rate limiting
Forgot credentials workflow
Navigation drawer interface
Built-in credits screen

## ✨ Security Features

bcrypt password hashing
Password policy enforcement
SQL injection mitigation via ORM
Input validation with Pydantic
User enumeration protection
Login attempt throttling

## 🛠️ Requirements

Python 3.11 and dependencies:

pip install -r requirements.txt

## ▶️ Running the backend

python -m uvicorn server.main:app --reload

API documentation:

http://127.0.0.1:8000/docs

## ▶️ Running the client

python client/main.py

## 📁 Project structure

auth-system/
├── client/
│   ├── main.py
│   ├── screens.py
│   └── ui.kv
├── server/
│   ├── **init**.py
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE

## 🧠 Concepts covered

This project was built to practice the following Python fundamentals:

Object-oriented programming
Client-server architecture
REST API development
Database modeling with SQLAlchemy
Authentication systems
Password hashing with bcrypt
Input validation with Pydantic
Rate limiting
Secure coding practices
Package-based project organization

---

## 🪟 Windows Release

Prebuilt Windows executables are available on the Releases page.

Download:

AuthSystem_app.exe
start_server.exe
How to run
Launch start_server.exe
Wait until the console shows Uvicorn running on http://127.0.0.1:8000
Keep the server window open
Launch AuthSystem_app.exe

Windows may display a SmartScreen warning the first time you open the executables.
Click More info → Run anyway. This is normal for unsigned executables built with PyInstaller.

---

## ⚠️ Disclaimer

This project was built for educational and portfolio purposes only.

It is not intended for production use without additional security hardening.

## 👨‍💻 Author

Francesco Falone — personal project to learn software engineering, backend development, and cybersecurity.

## 📄 License

This project is licensed under the Apache License 2.0.
