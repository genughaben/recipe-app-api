from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_creatE_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@frankwolf.blog"
        password = "12345678"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
