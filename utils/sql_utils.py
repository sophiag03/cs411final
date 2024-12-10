from db import db
import logging
from utils.logger import configure_logger

logger = logging.getLogger(__name__)
configure_logger(logger)

def check_database_connection():
    """
    Check if the database connection is active by running a simple query.

    Args:
        None

    Raise:
        Exception: If the database does not exist or an error occurs.
    """
    try:
        with db.session.begin():
            db.session.execute("SELECT 1")
        logger.info("Database connection successful.")
    except Exception as e:
        logger.error("Database connection error: %s", str(e))
        raise

def check_table_exists(tablename: str):
    """
    Check if a specific table exists in the database.

    Args:
        tablename (str): The name of the table to check.

    Raises:
        Exception: If the table does not exist or an error occurs.
    """
    try:
        with db.session.begin():
            result = db.session.execute(f"SELECT 1 FROM {tablename} LIMIT 1")
            if result.rowcount == 0:
                raise Exception(f"Table '{tablename}' exists but is empty.")
        logger.info("Table '%s' exists.", tablename)
    except Exception as e:
        logger.error("Table check error: %s", str(e))
        raise
