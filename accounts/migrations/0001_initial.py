# Generated by Django 4.1.5 on 2023-01-13 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('position', models.CharField(max_length=225)),
                ('office', models.CharField(max_length=225)),
                ('age', models.IntegerField()),
                ('joining_date', models.DateField(null=True)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
