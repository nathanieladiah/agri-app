from django.contrib import admin

from .models import Batch, Birds, Day, Eggs, Feed, Month

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
	pass

@admin.register(Birds)
class BirdsAdmin(admin.ModelAdmin):
	pass

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
	pass

@admin.register(Eggs)
class EggsAdmin(admin.ModelAdmin):
	pass

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
	pass

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
	pass