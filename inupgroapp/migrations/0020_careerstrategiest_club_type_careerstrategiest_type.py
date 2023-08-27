# Generated by Django 4.1.6 on 2023-08-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inupgroapp', '0019_clubdetails_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='careerstrategiest',
            name='club_type',
            field=models.CharField(choices=[('jobs', 'Jobs'), ('clubs', 'Clubs')], default='jobs', max_length=20),
        ),
        migrations.AddField(
            model_name='careerstrategiest',
            name='type',
            field=models.CharField(choices=[('school', 'School'), ('college', 'College'), ('institute', 'Institute')], default='school', max_length=20),
        ),
    ]