
# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import movie

@admin.register(movie)
class movie_infoAdmin(ImportExportModelAdmin):
    pass