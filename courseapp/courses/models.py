from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
class User(AbstractUser):
    pass

# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True,null=True)
    update_date = models.DateField(auto_now=True,null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return  self.name


class Course(BaseModel):
    subject = models.CharField(max_length=255, null= False)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/%y/%m')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_query_name= 'courses')
    tags = models.ManyToManyField('Tag')


    def  __str__(self):
        return self.subject
    class Meta:
        unique_together = ('subject', 'category')

class Lesson(BaseModel):
    subject = models.CharField(max_length=255, null= False)
    content = RichTextField()
    image = models.ImageField(upload_to='lessons/%y/%m')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    class Meta:
        unique_together = ('subject', 'course')


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique= True)

    def __str__(self):
        return self.name