# Generated by Django 3.2 on 2022-06-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to='users/', verbose_name='Аватарка'),
        ),
    ]