from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
	# avatar = models.ImageField(upload_to='avatars/', default='avatar.svg')

	def __str__(self):
		return f'{self.username}'

	# def get_absolute_url(self):
	# 	return reverse('profile', args=[str(self.username)])