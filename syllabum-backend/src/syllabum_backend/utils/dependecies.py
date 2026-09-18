from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status, Request
from syllabum_backend.auth import security
from syllabum_backend.db.connect_db import get_session
from syllabum_backend.models.user_models import User
from sqlmodel import Session

oauth2_scheme = OAuth2PasswordBearer("/login")


def get_current_user(request: Request, session: Session = Depends(get_session)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Inválido ou Expirado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    payload = security.decode_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Inválido ou Expirado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Inválido ou Expirado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Inválido ou Expirado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
