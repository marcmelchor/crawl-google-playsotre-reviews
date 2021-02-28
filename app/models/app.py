from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class AppManager(models.Manager):
    def save_app(self, android_app_id):
        try:
            app_object = super().get(app_id=android_app_id)
            print(f'The application {android_app_id} already exists.')

            return app_object
        except ObjectDoesNotExist:
            app_object = super().create(app_id=android_app_id)
            print(f'The application {android_app_id} has been saved.')

            return app_object


class App(models.Model):
    app_id = models.CharField(max_length=250, unique=True)

    objects = AppManager()

    def __str__(self):
        return self.app_id

    def __unicode__(self):
        return '/%s/' % self.app_id
