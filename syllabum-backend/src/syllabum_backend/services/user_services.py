from sqlmodel import Session, select, or_, and_
from syllabum_backend.auth import security
from syllabum_backend.models.user_models import User
from syllabum_backend.schemas.user_schemas import UserInfo, UserUpdate, UserForms
from datetime import datetime, timezone


def list_users(session: Session) -> list[UserInfo] | None:
    statement = select(User)
    users_list = list(session.exec(statement).all())
    if len(users_list) == 0:
        return None
    users_info: list[UserInfo] = [UserInfo.model_validate(user) for user in users_list]
    return users_info


def get_user_by_id(user_id: int, session: Session) -> UserInfo | None:
    user = session.get(User, user_id)
    if not user:
        return None
    return UserInfo.model_validate(user)


def create_user(data: UserForms, session: Session) -> tuple[UserInfo, str] | None:
    statement = select(User).where(
        or_(User.username == data.username, User.email == data.email)
    )
    user = session.exec(statement).first()
    if user:
        return None
    data.pwd = security.encode_password(data.pwd)
    new_user = User.model_validate(data)
    unhashed_token, hashed_token, token_expiry = security.generate_temp_token()
    new_user.email_verification_token = hashed_token
    new_user.email_verification_token_expiry = token_expiry
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return UserInfo.model_validate(new_user), unhashed_token


def update_user(data: UserUpdate, user: User, session: Session) -> UserInfo:
    dumped_data = data.model_dump()
    for attribute, value in dumped_data.items():
        setattr(user, attribute, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return UserInfo.model_validate(user)


def delete_user(user_id: int, session: Session) -> bool:
    user = session.get(User, user_id)
    if not user:
        return False
    session.delete(user)
    session.commit()
    return True


def login_user(data: UserForms, session: Session) -> tuple[UserInfo, str, str] | None:
    statement = select(User).where(
        or_(User.username == data.username, User.email == data.email)
    )
    user = session.exec(statement).first()
    if not user:
        return None
    assert user.id is not None
    is_password_correct = security.compare_password(data.pwd, user.pwd)
    if not is_password_correct:
        return None
    rt, hashed_rt = security.generate_refresh_token(user.id)
    access_token = security.generate_access_token(user.id, user.username, user.email)
    user.refresh_token = hashed_rt
    session.add(user)
    session.commit()
    session.refresh(user)
    return UserInfo.model_validate(user), access_token, rt


def verify_email(token: str, session: Session) -> bool:
    hashed_token = security.hash_token(token)
    statement = select(User).where(
        User.email_verification_token == hashed_token,
    )
    user = session.exec(statement).first()
    if (
        not user
        or not user.email_verification_token_expiry
        or user.email_verification_token_expiry < datetime.now(timezone.utc)
    ):
        return False
    user.is_email_verified = True
    user.email_verification_token = None
    user.email_verification_token_expiry = None
    session.add(user)
    session.commit()
    session.refresh(user)
    return True


def verify_forgot_pwd_request(token: str, new_pwd: str, session: Session) -> bool:
    hashed_token = security.hash_token(token)
    statement = select(User).where(
        User.forgot_password_token == hashed_token,
    )
    user = session.exec(statement).first()
    if (
        not user
        or not user.forgot_password_token_expiry
        or user.forgot_password_token_expiry < datetime.now(timezone.utc)
    ):
        return False
    is_pwd_same = security.compare_password(new_pwd, user.pwd)
    if is_pwd_same:
        return False
    user.pwd = security.encode_password(new_pwd)
    user.forgot_password_token = None
    user.forgot_password_token_expiry = None
    session.add(user)
    session.commit()
    session.refresh(user)
    return True


def regenerate_email_verification_token(user: User, session: Session) -> str:
    unhashed_token, hashed_token, token_expiry = security.generate_temp_token()
    user.email_verification_token = hashed_token
    user.email_verification_token_expiry = token_expiry
    session.add(user)
    session.commit()
    session.refresh(user)
    return unhashed_token


def regenerate_forgot_password_token(email: str, session: Session) -> str | None:
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()
    if not user:
        return None
    unhashed_token, hashed_token, token_expiry = security.generate_temp_token()
    user.forgot_password_token = hashed_token
    user.forgot_password_token_expiry = token_expiry
    session.add(user)
    session.commit()
    session.refresh(user)
    return unhashed_token
