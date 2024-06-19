from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import Account
from .models import Address
from rest_framework.authtoken.models import Token


class AddressAPITestCase(APITestCase):
    def setUp(self):
        self.user = Account.objects.create_user(username='testuser', password='testpassword')
        self.address = Address.objects.create(user=self.user, street="88-1", city="흥덕구", state="청주시", postal_code="12345", country="대한민국")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_addresses_unauthorized(self):
        self.client.logout()
        url = reverse('address-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_addresses(self):
        url = reverse('address-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_address(self):
        url = reverse('create-user-address', kwargs={'user_id': self.user.id})
        data = {
            'street': "99", 
            'city': "강남구",
            'state': "서울시",
            'postal_code': "12346",
            'country': "대한민국"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_update_address(self):
        url = reverse('address-detail', kwargs={'pk': self.address.pk}) + "update"
        data = {
            'street': "88-2",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.address.refresh_from_db()
        self.assertEqual(self.address.street, "88-2")

    def test_delete_address(self):
        url = reverse('address-detail', kwargs={'pk': self.address.pk}) + "delete"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Address.objects.filter(pk=self.address.pk).exists())