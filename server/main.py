from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

import time

from server.database import (
    engine,
    Base,
    SessionLocal
)

from server.schemas import (
    UserCreate,
    UserLogin
)

from server.models import User

from server.auth import (
    hash_password,
    verify_password,
    validate_password
)


app = FastAPI()

login_attempts = {}


Base.metadata.create_all(
    bind=engine
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/")
def home():

    return {
        "status": "online"
    }


@app.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    if not validate_password(
        user.password
    ):

        raise HTTPException(
            status_code=400,
            detail="password troppo debole"
        )


    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()


    if existing_user:

        raise HTTPException(
            status_code=409,
            detail="username già esistente"
        )


    existing_email = db.query(User).filter(
        User.email == user.email
    ).first()


    if existing_email:

        raise HTTPException(
            status_code=409,
            detail="email già registrata"
        )


    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(
            user.password
        )
    )


    db.add(new_user)
    db.commit()


    return {
        "success": True,
        "message": "utente creato"
    }


@app.post("/login")
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):

    username = credentials.username


    if username not in login_attempts:

        login_attempts[username] = {
            "count": 0,
            "blocked_until": 0
        }


    attempt_data = login_attempts[
        username
    ]


    if time.time() < attempt_data[
        "blocked_until"
    ]:

        raise HTTPException(
            status_code=429,
            detail="troppi tentativi, riprova più tardi"
        )


    user = db.query(User).filter(
        User.username == username
    ).first()


    if not user or not verify_password(
        credentials.password,
        user.password_hash if user else ""
    ):

        attempt_data[
            "count"
        ] += 1


        if attempt_data[
            "count"
        ] >= 5:

            attempt_data[
                "blocked_until"
            ] = time.time() + 30


            attempt_data[
                "count"
            ] = 0


        raise HTTPException(
            status_code=401,
            detail="credenziali non valide"
        )


    attempt_data[
        "count"
    ] = 0


    return {
        "success": True,
        "message": "login riuscito"
    }
