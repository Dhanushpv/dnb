# Generated by Django 5.0.1 on 2024-01-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_register_adress_register_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='experice',
            new_name='experience',
        ),
        migrations.AddField(
            model_name='register',
            name='gender',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
