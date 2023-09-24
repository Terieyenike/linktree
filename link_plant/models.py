from django.db import models

# Create your models here.
class Profile(models.Model):
    BG_CHOICES = (
        ('red', 'Red'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)
    profile_img = models.CharField(max_length=100, default='http://placekitten.com/g/200/300')


    def __str__(self):
        return self.name


class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return f"{self.text} | {self.url}"