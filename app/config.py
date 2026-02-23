import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("MYSQL_DATABASE", "songvault")
    DB_USER = os.getenv("MYSQL_USER", "songvault_user")
    DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "songvault_pass")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False