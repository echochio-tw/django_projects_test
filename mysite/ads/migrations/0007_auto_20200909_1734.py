# Generated by Django 3.1 on 2020-09-09 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_auto_20200909_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='comments',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
