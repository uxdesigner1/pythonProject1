from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return self.title

class Model2(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE

    )

    def __str__(self):
        return self.title
