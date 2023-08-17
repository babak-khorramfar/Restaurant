# Generated by Django 4.2.4 on 2023-08-17 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_alter_food_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_type',
            field=models.CharField(choices=[('L', 'Lunch'), ('D', 'Dinner')], default='D', max_length=10),
        ),
    ]