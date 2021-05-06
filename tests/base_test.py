"""

BaseTest

This class should be a parent class to each non-unit test.
It allows intantiation of the database dynamically
and make sure that it is a new , blank database each time.

"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    def setUp(self):
        # Make sure that database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # Database is blankc
        with app.app_context():
            db.session.remove()
            db.drop_all()

