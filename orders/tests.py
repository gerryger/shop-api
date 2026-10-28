from django.contrib.auth.models import User
from django.test import TestCase


class SmokeTest(TestCase):
    def test_user_can_be_created(self):
        user = User.objects.create_user("alice", password="x")
        self.assertEqual(user.username, "alice")
