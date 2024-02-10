from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Photo(models.Model):
    entry = models.ForeignKey(Entry, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='entry_photos/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f"Photo for entry: {self.entry.title}"

