from fastapi import APIRouter, HTTPException, status, Depends, Response, BackgroundTasks
from sqlmodel import Session
from syllabum_backend.services import user_services, email_services
from syllabum_backend.db.connect_db import get_session
from syllabum_backend.utils.dependecies import get_current_user
from syllabum_backend.models.user_models import User
from syllabum_backend.schemas.user_schemas import UserInfo, UserForms, UserUpdate

router = APIRouter(prefix="/api/v1/user", tags=["User"])


@router.get("/")
def list_users(session: Session = Depends(get_session)):
    users_list = user_services.list_users(session)
    if not users_list:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There's no registered users to show.",
        )
    return {
        "status": status.HTTP_200_OK,
        "data": users_list,
        "detail": "Successfully found a list of registered users.",
    }


@router.get("/{user_id}")
def get_user_by_id(user_id: int, session: Session = Depends(get_session)):
    user = user_services.get_user_by_id(user_id, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found or doesn't exist.",
        )
    return {
        "status": status.HTTP_200_OK,
        "data": user,
        "detail": "Successfully found the user by id.",
    }


@router.post("/register")
def create_user(
    data: UserForms,
    background_tasks: BackgroundTasks,
    session: Session = Depends(get_session),
):
    result = user_services.create_user(data, session)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists."
        )
    user, token = result
    background_tasks.add_task(email_services.verification_email, user.email, token)
    return {
        "status": status.HTTP_200_OK,
        "data": user,
        "detail": "User successfully registered.",
    }


@router.put("/")
def update_user(
    data: UserUpdate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    upd_user = user_services.update_user(data, user, session)
    return {
        "status": status.HTTP_200_OK,
        "data": upd_user,
        "detail": "User Info updated successfully.",
    }


@router.delete("/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    result = user_services.delete_user(user_id, session)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found or doesn't exist.",
        )
    return {
        "status": status.HTTP_200_OK,
        "data": result,
        "detail": "User successfully deleted.",
    }


@router.post("/login")
def login_user(
    data: UserForms, response: Response, session: Session = Depends(get_session)
):
    result = user_services.login_user(data, session)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found or password is incorrect.",
        )
    user, access_token, refresh_token = result
    response.set_cookie(
        "access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=3600,
    )
    response.set_cookie(
        "refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=86400,
    )
    return {
        "status": status.HTTP_200_OK,
        "data": user,
        "detail": "User logged-in successfully.",
    }


@router.get("/verify-email/{token}")
def verify_email(token: str, session: Session = Depends(get_session)):
    result = user_services.verify_email(token, session)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found, token can be expired, or already verified.",
        )
    return {
        "status": status.HTTP_200_OK,
        "data": result,
        "detail": "User email verified successfully.",
    }


@router.post("/forgot-password/{token}")
def verify_forgot_pwd(
    token: str, new_pwd: str, session: Session = Depends(get_session)
):
    result = user_services.verify_forgot_pwd_request(token, new_pwd, session)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found, token can be expired, or new password is the same as the old password.",
        )
    return {
        "status": status.HTTP_200_OK,
        "data": result,
        "detail": "Changed password successfully.",
    }

@router.post("/resend-email")
def resend_email_verification(background_tasks: BackgroundTasks, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    token = user_services.regenerate_email_verification_token(user, session)
    background_tasks.add_task(email_services.verification_email, user.email, token)
    return {
            "status": status.HTTP_200_OK,
            "data": f"Just sent email to {user.email}",
            "detail": "Resent email successfully.",
        }

@router.post("/resend-forgot-password")
def resend_forgot_password_email(background_tasks: BackgroundTasks, email: str, session: Session = Depends(get_session)):
    token = user_services.regenerate_forgot_password_token(email, session)
    if not token: 
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found or doesn't exist.",
                )
    background_tasks.add_task(email_services.reset_password_email, email, token)
    return {
                "status": status.HTTP_200_OK,
                "data": f"Just sent email to {email}",
                "detail": "Resent email successfully.",
            }

 