# Generated by Django 3.2.20 on 2023-07-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpddiary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryentry',
            name='cpdCredits',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
