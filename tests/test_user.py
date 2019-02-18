import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    """
    Docstring
    """
    def setUp(self):
        """
        Method that runs before all other tests.
        """
        self.new_user = User(password = 'zagadat')

    def test_password_setter(self):
        """
        Method that test if the password setter works.
        """
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access(self):
        """
        Method that tests if passwords cannot be viewed by users.
        """
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        """
        Method that tests if passwords are being verified correctly.
        """
        self.assertTrue(self.new_user.verify_password('zagadat'))