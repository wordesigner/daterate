# Generated by Django 5.0.6 on 2024-06-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='ex',
            field=models.IntegerField(null=True),
        ),
    ]
