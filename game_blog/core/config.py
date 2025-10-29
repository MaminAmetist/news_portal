import os
from pathlib import Path
from .img_extension import IMG_EXTENSION_LIST
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig


SECRET_KEY = b"SECRET_KEY"
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

SQLALCHEMY_DATABASE_URL = 'sqlite:///./site.db'

ROOT_URL = Path(__file__).resolve().parent.parent
MEDIA_URL = os.path.join(ROOT_URL, 'media')
templates = Jinja2Templates(directory="templates")


TemplateResponse = templates.TemplateResponse


mail_conf = ConnectionConfig(
    MAIL_USERNAME="testaccountruslan",
    MAIL_PASSWORD="ihildpyppazpehje",
    MAIL_FROM="testaccountruslan@yandex.ru",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.yandex.ru",
    MAIL_FROM_NAME="Test Messages",
    MAIL_STARTTLS=True,  # заменяет MAIL_TLS
    MAIL_SSL_TLS=False,  # заменяет MAIL_SSL
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)
