# Generated by Django 3.2.8 on 2022-06-24 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiggy', '0003_alter_item_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='food_image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
