# Generated by Django 3.1.7 on 2021-02-28 09:18

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(max_length=250, unique=True)),
            ],
            managers=[
                ('objects_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.CharField(max_length=250)),
                ('user_name', models.CharField(max_length=250)),
                ('user_image', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('score', models.IntegerField()),
                ('thumbs_up_count', models.IntegerField()),
                ('review_created_version', models.CharField(max_length=10)),
                ('at', models.DateField()),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.app')),
            ],
        ),
    ]
