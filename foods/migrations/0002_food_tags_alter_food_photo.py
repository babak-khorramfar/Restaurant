# Generated by Django 4.2.4 on 2023-08-16 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='tags',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='food',
            name='photo',
            field=models.ImageField(default=None, upload_to='foods/'),
        ),
    ]
