# Generated by Django 2.2.24 on 2021-12-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210718_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='ingredients',
            field=models.TextField(blank=True, default='', null=True, verbose_name='ingredients'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='mode_d_emploi',
            field=models.TextField(blank=True, default='', null=True, verbose_name="mode d'emploi"),
        ),
    ]
