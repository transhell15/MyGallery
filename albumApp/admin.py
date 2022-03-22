from django.contrib import admin

from albumApp.models import (
    Category,
    Photo,
)


# Model created for Category for Admin Panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date_created"]
    list_editable = ["name"]


# Model created for Photo for Admin Panel
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "category", "description", "date_created"]
    list_editable = ["image", "category", "description"]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
