# SecureAuth Python 🔐

A full-stack authentication system built with Python, FastAPI, and Kivy, developed as a personal learning project to explore backend architecture, authentication systems, and secure software design.

![SQLite](https://img.shields.io/badge/SQLite-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Kivy](https://img.shields.io/badge/Kivy-UI-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)


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

## ⚠️ Disclaimer

This project was built for educational and portfolio purposes only.

It is not intended for production use without additional security hardening.

## 👨‍💻 Author

Francesco Falone — personal project to learn software engineering, backend development, and cybersecurity.

## 📄 License

This project is licensed under the MIT License.
