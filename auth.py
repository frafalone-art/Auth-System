import bcrypt
import re


def hash_password(password: str):

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return hashed.decode()


def verify_password(
    plain_password: str,
    hashed_password: str
):

    return bcrypt.checkpw(
        plain_password.encode(),
        hashed_password.encode()
    )


def validate_password(
    password: str
):

    if len(password) < 8:
        return False


    if not re.search(
        r"[A-Z]",
        password
    ):
        return False


    if not re.search(
        r"[a-z]",
        password
    ):
        return False


    if not re.search(
        r"\d",
        password
    ):
        return False


    return True