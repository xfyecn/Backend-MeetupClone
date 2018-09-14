# Generated by Django 2.1 on 2018-08-30 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=240)),
                ('office', models.CharField(max_length=240)),
                ('web_address', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
                ('about', models.TextField()),
                ('event_image', models.ImageField(upload_to='events/images')),
                ('location', models.CharField(max_length=240)),
                ('event_date', models.DateField()),
                ('ticket_amount_first', models.DecimalField(decimal_places=3, max_digits=1000)),
                ('ticket_amount_second', models.DecimalField(decimal_places=3, max_digits=1000)),
                ('event_time_start', models.CharField(max_length=5)),
                ('event_time_end', models.CharField(max_length=5)),
                ('chief_guest', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=0)),
                ('review', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_review', to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_category', to='events.EventCategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='company_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_company', to='events.CompanyInfo'),
        ),
    ]
