# Generated by Django 4.2 on 2023-07-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='image',
            field=models.ImageField(max_length=255, upload_to='images/'),
        ),
    ]
