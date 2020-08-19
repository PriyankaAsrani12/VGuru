from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200, blank=False)
    publish_date = models.DateField(default=timezone.now())
    author = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=100)
    article_link = models.URLField()

    def __str__(self):
        return self.name
