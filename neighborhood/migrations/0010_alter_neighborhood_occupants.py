# Generated by Django 4.0.5 on 2022-06-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0009_alter_post_hood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='occupants',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]