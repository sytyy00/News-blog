from django.contrib import admin
from main.models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    list_filter = ['date']
    list_display = ['title', 'date']
    search_fields = ['title']


admin.site.register(Articles, ArticlesAdmin)
