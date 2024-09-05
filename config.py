import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    DEBUG = os.getenv('DEBUG', True)


class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class PostgresConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/transaction')


def get_config():
    db_type = os.getenv('DB_TYPE', 'sqlite').lower()
    if db_type == 'postgres':
        return PostgresConfig
    return SQLiteConfig
