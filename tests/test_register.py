def test_register_success(client, valid_user):
    response = client.post("/register", json=valid_user)

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_register_weak_password_rejected(client, valid_user):
    valid_user["password"] = "weak"

    response = client.post("/register", json=valid_user)

    assert response.status_code == 400
    assert "debole" in response.json()["detail"]


def test_register_duplicate_username_rejected(client, valid_user):
    client.post("/register", json=valid_user)

    second_user = valid_user.copy()
    second_user["email"] = "altra_email@example.com"

    response = client.post("/register", json=second_user)

    assert response.status_code == 409
    assert "username" in response.json()["detail"]


def test_register_duplicate_email_rejected(client, valid_user):
    client.post("/register", json=valid_user)

    second_user = valid_user.copy()
    second_user["username"] = "altro_utente"

    response = client.post("/register", json=second_user)

    assert response.status_code == 409
    assert "email" in response.json()["detail"]
