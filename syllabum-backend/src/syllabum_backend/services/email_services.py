import smtplib
from email.message import EmailMessage
from os import getenv
from dotenv import load_dotenv

load_dotenv()

MAILTRAP_HOST = getenv("MAILTRAP_HOST")
MAILTRAP_PORT = getenv("MAILTRAP_PORT")
MAILTRAP_USER = getenv("MAILTRAP_USER")
MAILTRAP_PASS = getenv("MAILTRAP_PASS")
MAIL_FROM = getenv("MAIL_FROM")


def send_email_message(email_to: str, subject: str, html_content: str):
    if (
        not MAILTRAP_HOST
        or not MAILTRAP_PORT
        or not MAILTRAP_USER
        or not MAILTRAP_PASS
        or not MAIL_FROM
    ):
        return None
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = MAIL_FROM
    message["To"] = email_to
    message.add_alternative(html_content, subtype="html")
    with smtplib.SMTP(MAILTRAP_HOST, int(MAILTRAP_PORT)) as server:
        server.starttls()
        server.login(MAILTRAP_USER, MAILTRAP_PASS)
        server.send_message(message)


def verification_email(email_to: str, token: str):
    url = f"http://127.0.0.1:8000/api/v1/user/verify-email/{token}"
    html = f"""
    <h2>Bem-vindo!</h2>
    <p>Clique no link abaixo para verificar sua conta:</p>
    <a href="{url}" target="_blank">Verificar E-mail</a>
    """
    send_email_message(email_to, "Verificação de Email", html)


def reset_password_email(email_to: str, token: str):
    url = f"http://127.0.0.1:8000/api/v1/user/forgot-password/{token}"
    html = f"""
    <h2>Bem-vindo!</h2>
    <p>Clique no link abaixo para poder reiniciar sua senha:</p>
    <a href="{url}" target="_blank">Forgot Password</a>
    """
    send_email_message(email_to, "Recuperação de Senha", html)


