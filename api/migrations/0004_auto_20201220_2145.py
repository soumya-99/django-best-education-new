# Generated by Django 3.0.8 on 2020-12-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_subscriptionform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedataforintro',
            name='image',
            field=models.ImageField(blank=True, upload_to='carousel_images'),
        ),
    ]
