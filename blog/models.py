from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]  # self is use when inside a class and the function wants to use the value of the class

    def __str__(self):
        return self.title