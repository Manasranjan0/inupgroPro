# Generated by Django 4.1.6 on 2023-08-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inupgroapp', '0006_alter_host_userdata_email_or_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host_userdata',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
