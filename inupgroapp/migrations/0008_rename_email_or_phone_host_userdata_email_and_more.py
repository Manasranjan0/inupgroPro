# Generated by Django 4.1.6 on 2023-08-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inupgroapp', '0007_alter_host_userdata_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host_userdata',
            old_name='email_Or_Phone',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='host_userdata',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
