from django.db import models

class Userdetails(models.Model):
    username = models.CharField(max_length=14)
    password = models.CharField(max_length=14)

class Post(models.Model):
    userdetails = models.ForeignKey(Userdetails, on_delete = models.CASCADE,default = '')
    title = models.CharField(max_length=50,blank=True)
    date_pub = models.DateField()
    content = models.TextField(blank = True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title

