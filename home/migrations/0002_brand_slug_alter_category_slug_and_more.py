# Generated by Django 4.2.1 on 2023-05-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.CharField(default=1, max_length=500, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]