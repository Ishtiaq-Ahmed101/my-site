# Generated by Django 3.2.16 on 2022-12-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_rename_item_imageg_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSA7GbKZJfH2z_BfU46jgCuiv2y73UaR0gpQg&usqp=CAU', max_length=1000),
        ),
    ]
