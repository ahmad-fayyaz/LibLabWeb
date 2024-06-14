from django.db import models
from django.urls import reverse

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('document_detail', args=[self.slug])

    def __str__(self):
        return self.title
