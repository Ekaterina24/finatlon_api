from django.db import models
from django.utils import timezone
from  embed_video.fields  import  EmbedVideoField

class New(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.ipg')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Tape(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video = EmbedVideoField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return self.title


class Review(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return '{}, {}'.format(self.name, self.title)


class Answer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.name, self.email)



