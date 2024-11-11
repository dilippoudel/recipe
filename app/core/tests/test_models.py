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

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        """Test the user without an email raise a Value error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Test@123')

    def test_create_new_super_user(self):
        """Test creating a superuser in the system."""
        email = 'superuser@example.com'
        password = 'SuperUser@123'
        user = get_user_model().objects.create_superuser(email, password)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
