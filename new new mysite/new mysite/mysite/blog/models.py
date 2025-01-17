from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class PublishedManager(models.Manager):
      def get_queryset(self):
           return super().get_queryset()\
                 .filter(status=Post.Status.PUBLISHED)
class Post(models.Model):
    class Status(models.TextChoices):
         DRAFT='DF','DRAFT'
         PUBLISHED='PB','PUUBLISHED'
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    author=models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(default=datetime.now,blank=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.DRAFT)
    objects=models.Manager()
    publisheed=PublishedManager()
    class Meta:
        ordering= ['-publish']
        indexes=[
            models.Index(fields=['-publish']),
        ]


    def __str__ (self):
        return self.title
