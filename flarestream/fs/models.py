from django.db import models

# Create your models here.
class userdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    password=models.CharField(max_length=264)

    def __str__(self):
        return self.email

class subdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    sub=models.CharField(max_length=264)
    date=models.CharField(max_length=264)

    def __str__(self):
        return self.email

class albcounter(models.Model):
    aid=models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.aid

class srtmvcounter(models.Model):
    sid=models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.sid

class album(models.Model):
    aid=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    filesall=models.FileField(upload_to='')
    title=models.CharField(max_length=264)
    upiid=models.CharField(max_length=264)
    desc=models.CharField(max_length=264)
    def __str__(self):
        return self.title

class short(models.Model):
    sid=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    filesall=models.FileField(upload_to='')
    title=models.CharField(max_length=264)
    upiid=models.CharField(max_length=264)
    desc=models.CharField(max_length=264)
    def __str__(self):
        return self.title
