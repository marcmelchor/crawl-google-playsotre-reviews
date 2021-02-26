from django.db import models
from .app import App


class Review(models.Model):
    app_id = models.ForeignKey(App, on_delete=models.CASCADE, blank=False, null=False)
    review_id = models.CharField(max_length=250)
    user_name = models.CharField(max_length=250)
    user_image = models.CharField(max_length=250)
    content = models.TextField()
    score = models.IntegerField()
    thumbs_up_count = models.IntegerField()
    review_created_version = models.CharField(max_length=10)
    at = models.DateField()

    def __str__(self):
        return self.review_id

    def __unicode__(self):
        return '/%s/' % self.review_id
