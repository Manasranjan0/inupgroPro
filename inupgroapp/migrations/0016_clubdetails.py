# Generated by Django 4.1.6 on 2023-08-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inupgroapp', '0015_instructorportfolioitem_delete_teacherportfolioitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100)),
                ('founded_year', models.DateField()),
                ('full_name', models.CharField(max_length=50)),
                ('total_registered_users', models.BigIntegerField()),
                ('total_seats', models.BigIntegerField()),
                ('total_applied_applications', models.BigIntegerField()),
                ('remaining_seats', models.BigIntegerField()),
                ('connectd_schools', models.IntegerField()),
                ('connected_colleges', models.IntegerField()),
                ('members', models.IntegerField()),
                ('club_details', models.TextField(max_length=1000)),
                ('aboutus', models.TextField(max_length=1000)),
            ],
        ),
    ]