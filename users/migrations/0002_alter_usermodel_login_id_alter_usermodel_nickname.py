# Generated by Django 4.1.1 on 2022-10-04 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='login_id',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='nickname',
            field=models.CharField(max_length=16),
        ),
    ]
