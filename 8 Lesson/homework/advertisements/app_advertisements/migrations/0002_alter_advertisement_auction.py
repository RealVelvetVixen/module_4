# Generated by Django 3.2.13 on 2023-07-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(help_text='Отметьте, если торг уместен', verbose_name='Торг'),
        ),
    ]
