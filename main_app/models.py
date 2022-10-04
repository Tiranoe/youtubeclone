from django.db import models

# Create your models here.
class Youtuber(models.Model):
    name = models.CharField(max_length = 50)
    img = models.CharField(max_length = 250)
    bio = models.CharField(max_length = 500)
    verified_youtuber = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']