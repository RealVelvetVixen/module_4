# Generated by Django 3.2.13 on 2023-07-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0002_alter_advertisement_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(help_text='Отметьте, если торг уместен.', verbose_name='Торг'),
        ),
    ]