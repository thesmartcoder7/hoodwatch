# Generated by Django 4.0.5 on 2022-06-19 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0002_post_business'),
        ('users', '0005_alter_profile_hood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='neighborhood.neighborhood'),
        ),
    ]