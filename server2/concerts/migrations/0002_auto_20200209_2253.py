# Generated by Django 3.0.2 on 2020-02-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='detail',
            field=models.TextField(null=True),
        ),
    ]
