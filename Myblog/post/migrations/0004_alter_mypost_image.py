# Generated by Django 3.2.7 on 2021-09-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_mypost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='image',
            field=models.ImageField(null=True, upload_to='posts_image/'),
        ),
    ]
