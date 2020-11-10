from django.urls import reverse, resolve

class TestUrls:

    def test_home_url(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'

    def test_customer_urls(self):
        path = reverse('customer', kwargs={'pk':10075})
        assert resolve(path).view_name == 'customer'

    def test_customers_url(self):
        path = reverse('customers')
        assert resolve(path).view_name == 'customers'
    
    def test_products_urls(self):
        path = reverse('products')
        assert resolve(path).view_name == 'products'

    # TODO: Add test for additional urls