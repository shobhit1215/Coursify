from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=200,null=True)
    price = models.IntegerField(null = False)
    discount = models.IntegerField(null=False,default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="files/thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    resourse = models.FileField(upload_to="files/resource")
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class Tag(models.Model):
    description = models.CharField(max_length=50,null=False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    


class Prerequisite(models.Model):
    description = models.CharField(max_length=50,null=False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    

class Learning(models.Model):
    description = models.CharField(max_length=50,null=False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Video(models.Model):
    title = models.CharField(max_length=100,null=False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    sno = models.IntegerField(null=False)
    video_id = models.CharField(max_length=20,null=False)
    is_preview = models.BooleanField(default=False)
