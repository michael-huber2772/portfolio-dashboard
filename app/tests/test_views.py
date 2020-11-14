from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from app.views import *
from mixer.backend.django import mixer
import pytest



@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        # These creates a test database so the primary keys change from what I
        # have on file so we have to go with the default of 1
        mixer.blend('app.Customer')
        cls.factory = RequestFactory()

    def test_customers_authenticated(self):
        """Test that the login required decorator is working on this view"""
        path = reverse('customers')
        request = self.factory.get(path)
        # Creates a new user instance
        request.user = mixer.blend(User)

        # This is where we call the function from the view
        response = customers(request)
        assert response.status_code == 200

    def test_customer_authenticated(self):
        """Test that the login required decorator is working on this view"""


        path = reverse('customer', kwargs={'pk': 1})
        request = self.factory.get(path)
        # Creates a new user instance
        request.user = mixer.blend(User)

        # This is where we call the function from the view
        response = customer(request, pk=1)
        assert response.status_code == 200

    def test_customer_unauthenticated(self):
        """Test that user who have not logged in get redirected to the login page"""

        path = reverse('customer', kwargs={'pk': 1})
        request = self.factory.get(path)
        # Creates a new user instance
        request.user = AnonymousUser()

        # This is where we call the function from the view
        response = customer(request, pk=1)
        # Looks to see that login is in the URL returned
        assert '/login' in response.url


        # TODO: Add tests for the other views