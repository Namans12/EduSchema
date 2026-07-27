import os

import mysql.connector


def create_connection():
    """Open a MySQL connection using credentials from the environment.

    Set these before running (see .env.example):
        EDUSCHEMA_HOST, EDUSCHEMA_USER, EDUSCHEMA_PASSWORD, EDUSCHEMA_DB
    """
    password = os.environ.get("EDUSCHEMA_PASSWORD")
    if password is None:
        raise RuntimeError(
            "EDUSCHEMA_PASSWORD is not set. "
            "Copy .env.example, fill it in, and export the variables before running."
        )

    connection = mysql.connector.connect(
        host=os.environ.get("EDUSCHEMA_HOST", "localhost"),
        user=os.environ.get("EDUSCHEMA_USER", "root"),
        password=password,
        database=os.environ.get("EDUSCHEMA_DB", "EduSchema"),
    )
    return connection
