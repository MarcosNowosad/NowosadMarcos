# Generated by Django 4.1.6 on 2023-03-31 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_image2_alter_post_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='', upload_to='blog/images/post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='', upload_to='blog/images/post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image4',
            field=models.ImageField(blank=True, default='', upload_to='blog/images/post'),
        ),
    ]
