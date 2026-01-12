from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    CHOICES_STATUS = (
        ('draft', 'Draft'),
        ('publish', 'publish')
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date="publish")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default='draft')


    class Meta:
        ordering = ("-publish",)


    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()


    def get_absolute_url(self):
        return reverse("")

post = Post.objects.all()
p_post = Post.published.all()