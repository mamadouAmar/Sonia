# Generated by Django 4.0.4 on 2022-05-17 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depense', '0002_auto_20211227_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depensemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]