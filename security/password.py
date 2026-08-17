import bcrypt


def generate_hashed_password(raw_password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=raw_password.encode("utf-8"), salt=salt)
    return hashed_password.decode("utf-8")


def verify_password(password_in: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password_in.encode("utf-8"), hashed_password.encode("utf-8"))
