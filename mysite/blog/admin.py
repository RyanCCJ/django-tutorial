from django.contrib import admin
from blog import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','date')
    ordering = ('-date',)

admin.site.register(models.User)
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)