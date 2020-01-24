from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    Comment_count = models.IntegerField(default = 0)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.Title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title)
        super(Post, self).save(*args, **kwargs)
