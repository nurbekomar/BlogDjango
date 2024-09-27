from django.db import models
from django.urls import reverse
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})
