# Generated by Django 4.0.4 on 2022-06-06 10:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TODO',
            new_name='Task',
        ),
    ]