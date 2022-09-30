# Generated by Django 4.1.1 on 2022-09-30 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.TextField(max_length=16)),
                ('nickname', models.TextField(max_length=16)),
                ('password', models.CharField(max_length=256)),
                ('password2', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=256)),
                ('user_images', models.ImageField(blank=True, null=True, upload_to='')),
                ('nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usermodel')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
