# Generated by Django 4.1.6 on 2023-03-31 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_imagepost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagepost',
            old_name='image',
            new_name='image1',
        ),
    ]
