from django.test import TestCase

from faker import Faker

from post.models import Post
from user.models import User
from user.tests import UserBuilder
from role.models import Role


class PostTestCase(TestCase):

    def setUp(self) -> None:
        user_builder = UserBuilder()
        faker = Faker()
        self.user = user_builder.user
        self.current_post = Post.objects.create(title=faker.name(), body=faker.text(),
                                                author=self.user)


    def tests_get_author_from_post(self):
        post = Post.objects.get(pk=self.current_post.id)
        self.assertEqual(post.author.id, self.user.id)
        self.assertEqual(post.author.name, self.user.name)
