from server.auth import hash_password, verify_password, validate_password


class TestHashPassword:

    def test_hash_is_not_plaintext(self):
        hashed = hash_password("Password123")
        assert hashed != "Password123"

    def test_same_password_gives_different_hashes(self):
        # bcrypt usa un salt random ogni volta: due hash della stessa
        # password devono essere diversi tra loro.
        hash_1 = hash_password("Password123")
        hash_2 = hash_password("Password123")
        assert hash_1 != hash_2


class TestVerifyPassword:

    def test_correct_password_verifies(self):
        hashed = hash_password("Password123")
        assert verify_password("Password123", hashed) is True

    def test_wrong_password_fails(self):
        hashed = hash_password("Password123")
        assert verify_password("WrongPassword1", hashed) is False


class TestValidatePassword:

    def test_valid_password_passes(self):
        assert validate_password("Password123") is True

    def test_too_short_fails(self):
        assert validate_password("Pw1") is False

    def test_missing_uppercase_fails(self):
        assert validate_password("password123") is False

    def test_missing_lowercase_fails(self):
        assert validate_password("PASSWORD123") is False

    def test_missing_digit_fails(self):
        assert validate_password("PasswordOnly") is False
