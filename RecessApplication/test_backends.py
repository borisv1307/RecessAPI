from unittest.mock import MagicMock
from RecessApplication.backends import UserBackend
from RecessApplication.models import CustomUser

# All test files should start with 'test_'
# Standard convention is test_<name of thing being tested>

# All test classes should start with 'Test'
class TestBackend:
    USERNAME = "TEST_USERNAME"
    PASSWORD = "TEST_PASSWORD"

    def mock_user_backend(self):
        user_backend = UserBackend()
        user_backend.get_user = MagicMock(return_value=self.mock_user())
        return user_backend

    def mock_user(self):
        user = CustomUser()
        user.username = TestBackend.USERNAME
        user.password = TestBackend.PASSWORD
        return user

    # All tests should start with 'test_'
    def test_authenticate_success(self):
        user_backend = self.mock_user_backend()
        result = user_backend.authenticate(request=None, password=TestBackend.PASSWORD)
        assert result == self.mock_user()

    def test_authenticate_wrongPassword(self):
        user_backend = self.mock_user_backend()
        result = user_backend.authenticate(request=None, password="NOT_PASSWORD")
        assert result == None
