# Generated by Django 4.0.5 on 2022-06-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_tape_alter_new_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tape',
            name='description',
            field=models.TextField(default=False),
        ),
    ]
