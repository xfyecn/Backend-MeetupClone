# Generated by Django 2.1 on 2018-09-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180903_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/images'),
        ),
    ]
