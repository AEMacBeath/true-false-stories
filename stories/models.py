from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Story(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    tvote = models.ManyToManyField(User, related_name='story_tvote', blank=True)
    fvote = models.ManyToManyField(User, related_name='story_fvote', blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def number_of_tvotes(self):
        return self.tvote.count()

    def number_of_fvotes(self):
        return self.fvote.count()


class Comment(models.Model):
    post = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
