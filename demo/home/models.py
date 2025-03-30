from django.db import models
from django.contrib.auth import get_user_model
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

User = get_user_model()

class Article(Page):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    content = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("author"),  # This will use the UserChooserViewSet
        FieldPanel("content"),
    ]