from django.contrib import admin
from .models import App, Review


class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_id')
    search_fields = ('app_id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'review_id')
    search_fields = ('review_id',)


admin.site.register(App, AppAdmin)
admin.site.register(Review, ReviewAdmin)
