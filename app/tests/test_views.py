from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from app.views import *
from mixer.backend.django import mixer
import pytest



@pytest.mark.django_db
class TestViews:


    def test_customers_authenticated(self):
        """Test that the login required decorator is working on this view"""
        path = reverse('customers')
        request = RequestFactory().get(path)
        # Creates a new user instance
        request.user = mixer.blend(User)

        # This is where we call the function from the view
        response = customers(request)
        assert response.status_code == 200

    def test_customer_authenticated(self):
        """Test that the login required decorator is working on this view"""
        # These creates a test database so the primary keys change from what I
        # have on file so we have to go with the default of 1
        mixer.blend('app.Customer')

        path = reverse('customer', kwargs={'pk': 1})
        request = RequestFactory().get(path)
        # Creates a new user instance
        request.user = mixer.blend(User)

        # This is where we call the function from the view
        response = customer(request, pk=1)
        assert response.status_code == 200