# Generated by Django 3.1 on 2020-09-09 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20200909_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='content_type',
            field=models.CharField(blank=True, help_text='The MIMEType of the file', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='picture',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]
