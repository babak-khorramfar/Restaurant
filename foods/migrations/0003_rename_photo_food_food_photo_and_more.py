# Generated by Django 4.2.4 on 2023-08-16 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_food_tags_alter_food_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='photo',
            new_name='food_photo',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='tags',
            new_name='food_tags',
        ),
    ]
