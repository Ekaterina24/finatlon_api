# Generated by Django 4.0.5 on 2022-06-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_link_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
