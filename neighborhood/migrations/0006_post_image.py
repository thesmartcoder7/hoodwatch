# Generated by Django 4.0.5 on 2022-06-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0005_alter_neighborhood_occupants'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hood_posts/'),
        ),
    ]
