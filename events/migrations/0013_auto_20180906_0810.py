# Generated by Django 2.1 on 2018-09-06 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_eventcategory_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_image',
            new_name='image',
        ),
    ]
