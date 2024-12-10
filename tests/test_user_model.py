import unittest
from flask import Flask
from models.user_model import Users, db  # Import db from your app module

# Set up the Flask app for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class TestUsersModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #application context and initialize the database
        cls.app_context = app.app_context()
        cls.app_context.push()
        db.init_app(app)  # Initialize `db` with the Flask app
        db.create_all()  # Create the necessary tables

    @classmethod
    def tearDownClass(cls):
        #remove application context 
        db.session.remove()
        db.drop_all()  
        cls.app_context.pop()

    def setUp(self):
        #reset the database before each test
        db.session.remove()
        db.drop_all()
        db.create_all()

    def test_create_user_success(self):
        Users.create_user("testuser", "password123")
        user = Users.query.filter_by(username="testuser").first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")

    def test_create_user_duplicate_username(self):
        Users.create_user("testuser", "password123")
        with self.assertRaises(ValueError):
            Users.create_user("testuser", "password123")

    def test_check_password_success(self):
        Users.create_user("testuser", "password123")
        result = Users.check_password("testuser", "password123")
        self.assertTrue(result)

    def test_check_password_user_not_found(self):
        with self.assertRaises(ValueError):
            Users.check_password("unknownuser", "password123")

    def test_get_id_by_username_success(self):
        Users.create_user("testuser", "password123")
        user_id = Users.get_id_by_username("testuser")
        self.assertIsNotNone(user_id)

    def test_get_id_by_username_user_not_found(self):
        with self.assertRaises(ValueError):
            Users.get_id_by_username("unknownuser")

    def test_delete_user_success(self):
        Users.create_user("testuser", "password123")
        Users.delete_user("testuser")
        user = Users.query.filter_by(username="testuser").first()
        self.assertIsNone(user)

    def test_update_password_success(self):
        Users.create_user("testuser", "password123")
        Users.update_password("testuser", "newpassword456")
        result = Users.check_password("testuser", "newpassword456")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
