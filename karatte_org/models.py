from django.db import models

# Create your models here.
# class Image(models.Model):
#     image=models.ImageField(upload_to="img/%y")
#     def __str__(self):
#         return self.image
# class Gallery(models.Model):
#     name = models.CharField(max_length=200,null=True)
#     image = models.ImageField(upload_to='image',null=True,blank=True)
#     description = models.CharField(max_length=400,null=True)
#     def str(self):
#         return self.name