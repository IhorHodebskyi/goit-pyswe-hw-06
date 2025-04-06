
import psycopg2
from contextlib import contextmanager

DATABASE_URL = "postgresql://postgres:password@localhost:5432/test"


@contextmanager
def create_connection():
    """Create a database connection"""
    connect = None
    try:
        connect = psycopg2.connect(DATABASE_URL)
        yield connect
        connect.commit()
    except psycopg2.OperationalError as e:
        if connect:
            connect.rollback()
        raise RuntimeError(f"Error: {e}")
    finally:
        if connect:
            connect.close()



