from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django .contrib.auth import authenticate
class RegisterTestCase(TestCase):
    def test_register_success(self):
        self.client.post(
            reverse('user:register'),
            data={
                'username':'salom',
                'first_name':'Farrux',
                'last_name':'Fozilov',
                'email':'salom@mail.ru',
                'password':'12345',
                'password_confirm':'12345'
                }
        )
        user_count=User.objects.all().count()

        user=User.objects.get(username='Farrux')

        self.assertEqual(user_count,1)
        self.assertEqual(user.first_name,'Farrux')
        self.assertEqual(user.last_name,'Fozilov')
        self.assertEqual(user.email,'salom@mail.ru')    
        self.assertNotEqual(user.password,'12345')
        self.assertEqual(user.check_password('12345'))




class LoginTestCase(TestCase):
    def setUp(self):
        
        self.username = 'users'
        self.password = '11111'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        
        login= reverse('login')  
        response = self.client.post(login, {'username': self.username, 'password': self.password})
        
      
        self.assertEqual(response.status_code, 300)  
        self.assertTrue('_auth_user_id' in self.client.session)

