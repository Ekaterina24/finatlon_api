# Generated by Django 4.0.5 on 2022-06-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_review_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.DateField()),
                ('options', models.ManyToManyField(to='api.option')),
            ],
        ),
    ]
