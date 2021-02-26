from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class App(models.Model):
    app_id = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.app_id

    def __unicode__(self):
        return '/%s/' % self.app_id

    @classmethod
    def save_app(cls, android_app_id):
        try:
            app_object = cls.objects.get(app_id=android_app_id)
            print(f'The application {android_app_id} already exists.')

            return app_object
        except ObjectDoesNotExist:
            android_app = cls(app_id=android_app_id)
            app_object = android_app.save()
            print(f'The application {android_app_id} has been saved.')

            return app_object
