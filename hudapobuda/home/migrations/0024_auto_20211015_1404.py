# Generated by Django 3.1.10 on 2021-10-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20211015_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletterpage',
            name='newsletter_id',
            field=models.TextField(blank=True, null=True, verbose_name='Mautic ID'),
        ),
        migrations.AddField(
            model_name='newsletterpage',
            name='newsletter_key',
            field=models.TextField(blank=True, null=True, verbose_name='Mautic key'),
        ),
    ]
