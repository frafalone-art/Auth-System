import time

from server.main import login_attempts


def _register(client, user):
    client.post("/register", json=user)


def test_login_success(client, valid_user):
    _register(client, valid_user)

    response = client.post(
        "/login",
        json={
            "username": valid_user["username"],
            "password": valid_user["password"],
        },
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_login_wrong_password_rejected(client, valid_user):
    _register(client, valid_user)

    response = client.post(
        "/login",
        json={
            "username": valid_user["username"],
            "password": "PasswordSbagliata1",
        },
    )

    assert response.status_code == 401


def test_login_nonexistent_user_rejected(client):
    response = client.post(
        "/login",
        json={"username": "non_esiste", "password": "Password123"},
    )

    assert response.status_code == 401


def test_login_blocks_after_5_failed_attempts(client, valid_user):
    _register(client, valid_user)

    wrong_credentials = {
        "username": valid_user["username"],
        "password": "PasswordSbagliata1",
    }

    for _ in range(5):
        response = client.post("/login", json=wrong_credentials)
        assert response.status_code == 401

    # Il 6° tentativo deve essere bloccato dal rate limiting,
    # anche con la password corretta.
    response = client.post(
        "/login",
        json={
            "username": valid_user["username"],
            "password": valid_user["password"],
        },
    )

    assert response.status_code == 429


def test_login_unblocks_after_block_window_expires(client, valid_user):
    _register(client, valid_user)

    wrong_credentials = {
        "username": valid_user["username"],
        "password": "PasswordSbagliata1",
    }

    for _ in range(5):
        client.post("/login", json=wrong_credentials)

    assert login_attempts[valid_user["username"]]["blocked_until"] > time.time()

    # Simula la scadenza dei 30 secondi di blocco senza aspettare
    # davvero: manipoliamo direttamente il dizionario in memoria.
    login_attempts[valid_user["username"]]["blocked_until"] = time.time() - 1

    response = client.post(
        "/login",
        json={
            "username": valid_user["username"],
            "password": valid_user["password"],
        },
    )

    assert response.status_code == 200
