# Generated by Django 3.1 on 2020-09-10 09:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0008_auto_20200910_0627'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commentad',
            new_name='Comment',
        ),
    ]