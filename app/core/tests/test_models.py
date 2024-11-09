"""Test for models."""
# Testcase is the base class imported from django.test model \ 
# which is useable when the test comes with database integrations
from django.test import TestCase
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#django.contrib.auth.get_user_model

from django.contrib.auth import get_user_model


class ModelsTestUser(TestCase):
    """Test the creation of user with email successfully."""

    def test_create_user_with_email(self):
        """Test create user with email."""
        email = 'user@example.com'
        password = 'TestPass@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    

