# Generated by Django 4.1.6 on 2023-03-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_image3_post_image4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(default='', null=True, upload_to='blog/images/post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(default='', null=True, upload_to='blog/images/post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image4',
            field=models.ImageField(default='', null=True, upload_to='blog/images/post'),
        ),
    ]
