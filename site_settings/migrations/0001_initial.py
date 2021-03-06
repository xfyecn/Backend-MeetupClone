# Generated by Django 2.1 on 2018-08-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(upload_to='settings/banner')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Cms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField()),
                ('our_services', models.TextField()),
                ('terms', models.TextField()),
                ('contact_address', models.TextField()),
                ('contact_number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('website_title', models.CharField(max_length=200)),
                ('admin_address', models.TextField()),
                ('admin_email', models.EmailField(max_length=200)),
                ('facebook', models.URLField()),
                ('google_plus', models.URLField()),
                ('linkedin', models.URLField()),
                ('twitter', models.URLField()),
                ('website_logo', models.ImageField(upload_to='settings/logo')),
                ('banner_image', models.ImageField(upload_to='settings/banner')),
            ],
        ),
    ]
