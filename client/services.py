import re
import bcrypt
import smtplib
import secrets
import time

from email.mime.text import MIMEText
from kivy.storage.jsonstore import JsonStore


db = JsonStore("users.json")
remember_db = JsonStore("remember.json")


# ---------------- VALIDAZIONE ----------------

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)


# ---------------- DATABASE ----------------

def user_exists(username):
    return db.exists(username)


def save_user(username, email, password):
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    db.put(
        username,
        email=email,
        password=hashed.decode()
    )


def verify_password(username, password):
    data = db.get(username)

    return bcrypt.checkpw(
        password.encode(),
        data["password"].encode()
    )


# ---------------- REMEMBER ----------------

def save_remember_user(username):
    remember_db.put(
        "remember",
        user=username
    )


def delete_remember_user():
    if remember_db.exists("remember"):
        remember_db.delete("remember")


def get_remembered_user():
    if remember_db.exists("remember"):
        return remember_db.get("remember")["user"]

    return None


# ---------------- RESET TOKEN ----------------

def create_reset_token():
    token = secrets.token_hex(3)

    expiry = time.time() + 600

    return token, expiry


# ---------------- EMAIL ----------------

def send_reset_email(
    sender_email,
    sender_password,
    to_email,
    token
):
    body = f"""
Hai richiesto il reset password.

Codice: {token}

Valido per 10 minuti.
"""

    msg = MIMEText(body)

    msg["Subject"] = "Reset Password"
    msg["From"] = sender_email
    msg["To"] = to_email

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(
        sender_email,
        sender_password
    )

    server.send_message(msg)

    server.quit()
