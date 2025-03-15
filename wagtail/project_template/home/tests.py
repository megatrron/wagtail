
from django.test import TestCase
from wagtail.models import Page
from home.models import HomePage


class HomeSetUpTests(TestCase):
    """
    Tests steps needed by follow up tests
    """

    def test_root_create(self):
        Page.objects.get(pk=1)

    def test_homepage_create(self):
        root_page = Page.objects.get(pk=1)
        self.homepage = HomePage(title='Home')
        root_page.add_child(instance=self.homepage)


class HomeTests(TestCase):
    """
    Class for testing homepage logic
    """

    def setUp(self):
        """
        Set up the testing environment.
        """
        root_page = Page.objects.get(pk=1)
        self.homepage = HomePage(title='Home')
        root_page.add_child(instance=self.homepage)
        
    def test_your_test(self):
        """
        Tests if BlogIndexPage can be created.
        """
        raise NotImplementedError("The tests are not implemented yet.")