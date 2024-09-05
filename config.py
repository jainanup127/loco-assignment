# config.py
import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    DEBUG = os.getenv('DEBUG', True)


class SQLiteConfig(Config):
    """Configuration for in-memory SQLite database"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class PostgresConfig(Config):
    """Configuration for PostgreSQL database"""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/transaction')


def get_config():
    """Returns the configuration class based on the environment"""
    db_type = os.getenv('DB_TYPE', 'sqlite').lower()
    if db_type == 'postgres':
        return PostgresConfig
    return SQLiteConfig
