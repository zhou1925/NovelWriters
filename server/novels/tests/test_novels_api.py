from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from ..serializers import NovelSerializer
from ..models import Novel



NOVELS_URL = reverse('novels:novel-list')

PASSWORD = 'pAssw0rd!'

def create_user(username='usertest', password=PASSWORD):
    return get_user_model().objects.create_user(
        username=username,
        first_name='Test',
        last_name='User',
        password=password
    )

class PrivateNovelApiTest(APITestCase):
    """ Test the authorized user novels API """
    def setUp(self):
        self.user = create_user()
        response = self.client.post(reverse('users:log_in'), data={
            'username': self.user.username,
            'password': PASSWORD
        })
        self.access = response.data['access']
    
    def test_user_can_retrieve_novels(self):
        """ The user can retrieve novels """
        Novel.objects.create(author=self.user, title='oliver twist', description='description novel')
        Novel.objects.create(author=self.user, title='El psicoanalista', description='description novel')
        Novel.objects.create(author=self.user, title='Sherlock holmes', description='description novel')

        response = self.client.get(NOVELS_URL,
            HTTP_AUTHORIZATION=f'Bearer {self.access}'
        )
        novels = Novel.objects.all()
        serializer = NovelSerializer(novels, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_user_can_create_novel(self):
        """ Test user can create a new novel """
        payload = {'title': 'new best seller novel', 'description': 'novel description'}
        self.client.post(NOVELS_URL, payload, HTTP_AUTHORIZATION=f'Bearer {self.access}')
        novel_exists = Novel.objects.filter(author=self.user, title=payload['title']).exists()
        self.assertTrue(novel_exists)
    
    def test_user_create_invalid_novel(self):
        """ Test the user create a novel with invalid data """
        data = {'name': '', 'title': '', 'description': ''}
        response = self.client.post(NOVELS_URL, data, HTTP_AUTHORIZATION=f'Bearer {self.access}')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)