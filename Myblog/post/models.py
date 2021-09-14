from django.db import models

# Create your models here.
class MyPost(models.Model):
	title=models.CharField(max_length=55)
	content=models.TextField()
	image=models.ImageField(upload_to="posts_image/")
	def __str__(self):
		return "Titre : {}, Image :".format(self.title,self.image)