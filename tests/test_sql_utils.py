import unittest
from unittest.mock import patch, MagicMock
from utils.sql_utils import check_database_connection, check_table_exists

class TestSQLUtils(unittest.TestCase):

    @patch('utils.sql_utils.db.session')
    def test_check_database_connection_success(self, mock_session):
        # Mock a successful database connection
        mock_session.begin.return_value.__enter__.return_value = mock_session
        mock_session.execute.return_value = None

        try:
            check_database_connection()
        except Exception as e:
            self.fail(f"check_database_connection() raised an exception unexpectedly: {e}")

    @patch('utils.sql_utils.db.session')
    def test_check_database_connection_failure(self, mock_session):
        # Mock a database connection failure
        mock_session.begin.side_effect = Exception("Database connection error")

        with self.assertRaises(Exception) as context:
            check_database_connection()

        self.assertIn("Database connection error", str(context.exception))

    @patch('utils.sql_utils.db.session')
    def test_check_table_exists_success(self, mock_session):
        # Mock a successful table check
        mock_session.begin.return_value.__enter__.return_value = mock_session
        mock_result = MagicMock()
        mock_result.rowcount = 1
        mock_session.execute.return_value = mock_result

        try:
            check_table_exists("test_table")
        except Exception as e:
            self.fail(f"check_table_exists() raised an exception unexpectedly: {e}")

    @patch('utils.sql_utils.db.session')
    def test_check_table_exists_table_empty(self, mock_session):
        # Mock a table that exists but is empty
        mock_session.begin.return_value.__enter__.return_value = mock_session
        mock_result = MagicMock()
        mock_result.rowcount = 0
        mock_session.execute.return_value = mock_result

        with self.assertRaises(Exception) as context:
            check_table_exists("empty_table")

        self.assertIn("Table 'empty_table' exists but is empty", str(context.exception))

    @patch('utils.sql_utils.db.session')
    def test_check_table_exists_failure(self, mock_session):
        # Mock a table existence check failure
        mock_session.begin.side_effect = Exception("Table check error")

        with self.assertRaises(Exception) as context:
            check_table_exists("nonexistent_table")

        self.assertIn("Table check error", str(context.exception))

if __name__ == '__main__':
    unittest.main()
