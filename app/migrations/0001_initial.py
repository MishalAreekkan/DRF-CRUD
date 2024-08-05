# Generated by Django 5.0.7 on 2024-07-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=500)),
                ('domain', models.CharField(max_length=500)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
