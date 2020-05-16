from django.db import models

# Create your models here.


class movie(models.Model):
	id   	= models.IntegerField(primary_key=True ) 
	color		= models.TextField(max_length=200 )
	director_name	= models.TextField(max_length=200 )
	movie_title= models.TextField(max_length=200 )
	
	
	#imdbRating	= models.IntegerField(null=True) 
	#year=  models.IntegerField(null=True) 
	
	#url	= models.TextField(max_length= 100000)

	def __str__ (self):
		return (self.movie_title)