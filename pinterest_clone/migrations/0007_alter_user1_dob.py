# Generated by Django 3.2.6 on 2021-11-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest_clone', '0006_alter_user1_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='dob',
            field=models.DateField(default=1984),
        ),
    ]