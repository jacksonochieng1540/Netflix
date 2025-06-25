from django.contrib import admin

# Register your models here.
from.models import Movie,MovieList

admin.site.register(Movie)
admin.site.register(MovieList)