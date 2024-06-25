from operator import mod
from django.conf import settings
from django.db import models


class Batch(models.Model):
	house_number = models.IntegerField()
	date_housed = models.DateField()
	original_count = models.IntegerField()
	breed = models.CharField(max_length=50)
	# user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	# current_count

	class Meta:
		verbose_name_plural = 'batches'


class Month(models.Model):
	month = models.CharField(max_length=20)
	batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
	
	# Start and end count should be updated using the records from daily

	# start_count = models.IntegerField()
	# end_count = models.IntegerField()

class Day(models.Model):
	date = models.DateField()
	month = models.ForeignKey(Month, on_delete=models.CASCADE)
	# eggs = models.ForeignKey(Eggs, on_delete=models.CASCADE)
	# feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
	# birds = models.ForeignKey(Birds, on_delete=models.CASCADE)

	# Might need to put a signal when a day is updated to update the end count 
	# of a month

class Eggs(models.Model):
	day = models.ForeignKey(Day, on_delete=models.CASCADE)
	collection_1 = models.IntegerField(default=0)
	collection_2 = models.IntegerField(default=0)
	collection_3 = models.IntegerField(default=0)
	cracked = models.IntegerField(default=0)
	
	# methods
	# total
	# add to cracked

	class Meta:
		verbose_name_plural = 'eggs'

class Feed(models.Model):
	day = models.ForeignKey(Day, on_delete=models.CASCADE)
	mash = models.DecimalField(max_digits=5, decimal_places=2)
	shells = models.DecimalField(max_digits=5, decimal_places=2)

	# methods 
	# total

	class Meta:
		verbose_name_plural = 'feed'


class Birds(models.Model):
	day = models.ForeignKey(Day, on_delete=models.CASCADE)
	died = models.IntegerField()
	cull = models.IntegerField()

	# methods 
	# total

	class Meta:
		verbose_name_plural = 'eggs'

