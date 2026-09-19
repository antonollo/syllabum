import jwt  #  Geração de Access Token e Refresh Token
import bcrypt  #  Codificação de Senhas
import secrets  #  Geração de Tokens temporários
import hashlib
from datetime import datetime, timezone, timedelta
from os import getenv
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")


#  Codificação de Senha
def encode_password(pwd: str) -> str:
    enc_pwd = pwd.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(enc_pwd, salt).decode()


#  Comparação de Senha
def compare_password(pwd: str, user_pwd: str) -> bool:
    return bcrypt.checkpw(pwd.encode(), user_pwd.encode())


#  Decodificação de Token
def decode_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError as e:
        raise e


## Geração de AccessToken
def generate_access_token(user_id: int, username: str, email: str) -> str:
    payload = {
        "user_id": user_id,
        "username": username,
        "user_email": email,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    }
    return jwt.encode(payload, key=SECRET_KEY, algorithm=ALGORITHM)


## Geração de RefreshToken
def generate_refresh_token(user_id: int) -> tuple[str, str]:
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(days=1),
    }
    refresh_token = jwt.encode(payload, key=SECRET_KEY, algorithm=ALGORITHM)
    hashed_refresh_token = hashlib.sha256(refresh_token.encode()).hexdigest()
    return refresh_token, hashed_refresh_token


##  Geração de Temporary Tokens (para verificação de email e forgot password)
def generate_temp_token() -> tuple[str, str, datetime]:
    unhashed_token = secrets.token_urlsafe(32)
    hashed_token = hash_token(unhashed_token)
    token_expiry = datetime.now(timezone.utc) + timedelta(minutes=15)
    return unhashed_token, hashed_token, token_expiry


## Hashing para verificação de tokens
def hash_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()
