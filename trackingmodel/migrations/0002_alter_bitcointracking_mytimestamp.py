# Generated by Django 4.1.5 on 2023-01-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackingmodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitcointracking',
            name='mytimestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
