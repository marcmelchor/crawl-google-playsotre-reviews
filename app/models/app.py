from django.db import models


class App(models.Model):
    app_id = models.CharField(max_length=250)

    def __str__(self):
        return self.app_id

    def __unicode__(self):
        return '/%s/' % self.app_id
