from django.db import models
#from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='No description provided')
    video_file = models.FileField(upload_to='video/')

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service} on {self.date}"



class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/')
    description = models.TextField()

    def __str__(self):
        return self.title