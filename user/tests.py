from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


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
        user_count=User.objects.count()

        user=User.objects.get(username='salom')

        self.assertEqual(user_count,1)
        self.assertEqual(user.first_name,'Farrux')
        self.assertEqual(user.last_name,'Fozilov')
        self.assertEqual(user.email,'salom@mail.ru')    
        self.assertNotEqual(user.password,'12345')
        self.assertEqual(user.check_password('12345'))


    def test_username_field(self):
        response=self.client.post(
            reverse('user:register'),
            data={
                'username':'root',
                'first_name':'Farru',
                'last_name':'Fozilov',
                'email':'salom@mail.ru',
                'password':'12345',
                'password_confirm':'12345'
                }
        )
        form=response.context['form']


        user_count=User.objects.count()
        self.assertEqual(user_count,0)
        self.assertTrue('username' in form.errors)
        self.assertIn('username',form.errors.key())
        self.assertEqual(form.errors['username'],'username 5 va 30 oraligida bolish kerak')

    def test_password_field(self):
        response=self.client.post(
            reverse('user:register'),
            data={
                'username':'salom',
                'first_name':'Farru',
                'last_name':'Fozilov',
                'email':'salom@mail.ru',
                'password':'12345',
                'password_confirm':'12345'
                }
        )
        form=response.context['form']


        user_count=User.objects.count()
        self.assertEqual(user_count,0)
        self.assertTrue(form.errors)
        self.assertIn("password_confirm",form.errors.key())
        self.assertEqual(form.errors['password_confirm'],'parollar ikki hil bir biriga mos kelishi kerak')


    def test_email_field(self):
        response=self.client.post(
            reverse('user:register'),
            data={
                'username':'salom',
                'first_name':'Farru',
                'last_name':'Fozilov',
                'email':'salom@mail.ru',
                'password':'12345',
                'password_confirm':'12345'
                }
        )
        form=response.context['form']


        user_count=User.objects.count()
        self.assertEqual(user_count,0)
        self.assertTrue('email', form.errors)
        self.assertIn("email",form.errors.key())
     




class LoginTestCase(TestCase):
        def test_login_success(self):
             user=User.objects.create_user(username='salomim',first_name='Farrux',last_name='Fozilov')
             user.set_password('12344')
             user.save()

             self.client.post(
                reverse('user:login'),
                data={
                    'username':'salomim',
                    'password':'12344'
                })
             
             user_count=User.objects.count()
             self.assertEqual(user_count,1)

             user=get_user(username='salomim')
             self.assertTrue(user.is_authenticated)
        def test_username_field(self):
            response=self.client.post(
                    reverse('user:register'),
                    data={
                        'username':'salomim',
                        'first_name':'Farru',
                        'last_name':'Fozilov',
                        'email':'salom@mail.ru',
                        'password':'12344',
                        'password_confirm':'12344'
                        }
            )
            form=response.context['form']


            user_count=User.objects.count()
            self.assertEqual(user_count,0)
            self.assertTrue(form.errors)
            self.assertIn("username",form.errors.key())
            self.assertEqual(form.errors['username'],'username borr')     

                
