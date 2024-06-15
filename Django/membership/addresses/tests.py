from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.models import User
from .models import Address
from rest_framework_simplejwt.tokens import RefreshToken

class AddressesAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='password')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {self.token}")
        self.address = Address.objects.create(user=self.user, street='street1', city='city1')

    # 권한이 없는 경우 Test
    def test_get_addresses_unauthorized(self):
        self.client.logout()
        url = reverse('addresses')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_all_addresses(self):
        url = reverse('addresses')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_address(self):
        self.client.login(username="testuser2", password="password")
        url = reverse('addresses')

        data = {
            'street': 'street2',
            'city':'city2', 
            'state': 'state2',
            'postal_code': '3434',
            'country': 'korea', 
        }

        res = self.client.post(url, data)
        print(res.data)
        self.assertEqual(res.data['street'], 'street2')
        self.assertEqual(res.data['postal_code'], '3434')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    # setUp 에서 정의하고 만든 데이터를 수정해야한다.
    # 위의 create test에서 만든건 x
    def test_put_address_detail(self):
        self.client.login(username="testuser2", password="password")
        url = reverse('address_detail', kwargs={'address_id': 1})

        data = {
            'street': 'street2',
            'city':'city3', 
            'state': 'state3',
            'postal_code': '1234',
            'country': 'korea', 
        }

        res = self.client.put(url, data)
        self.assertEqual(res.data['postal_code'], '1234')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_address(self):
        self.client.login(username="testuser2", password="password")
        url = reverse('address_detail', kwargs={'address_id': 1})
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)