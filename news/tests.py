from django.test import TestCase
from django.urls import reverse
from .models import News

# Create your tests here.
class NewsModelTest(TestCase):
    def setUp(self):
        News.objects.create(title='this is a title', text='this is a text')
    
    def test_text_content(self):
        news=News.objects.get(id=1)
        expected_object_title=f'{news.title}'
        expected_object_text=f'{news.text}' 
        self.assertEqual(expected_object_title, 'this is a title')
        self.assertEqual(expected_object_text, 'this is a text')
    

class HomePageViewTest(TestCase):
    def setUp(self):
        News.objects.create(title='this is a title', text='this is a text')
    
    def test_view_url_exists_at_proper_location(self):
        resp=self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp=self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp=self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        
