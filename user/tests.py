from django.test import TestCase
from faker import Faker

from role.models import Role
from user.models import User


class UserBuilder:
    RAMON_EMAIL = 'ramon@meuemail.com'

    def __init__(self):
        faker = Faker()
        self.__role = Role.objects.create(title="SUPERUSER", description="can do anything")
        self.__user = User.objects.create(name=faker.name(), password="12345", email=self.RAMON_EMAIL,
                                          role=self.role)

    @property
    def role(self):
        return self.__role

    @property
    def user(self):
        return self.__user


class TestUser(TestCase):
    ONE_TO_FIVE_IN_MD5 = "827ccb0eea8a706c4c34a16891f84e7b"

    def setUp(self) -> None:
        user_builder = UserBuilder()

    def test_password_crypt(self) -> None:
        ramon = User.objects.get(email=UserBuilder.RAMON_EMAIL)
        self.assertEqual(ramon.password, self.ONE_TO_FIVE_IN_MD5)
