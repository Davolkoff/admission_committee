# Generated by Django 4.0.2 on 2023-06-19 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_operators_current_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='operators',
            name='current_ticket',
            field=models.IntegerField(blank=True, null=True, verbose_name='Текущий посетитель'),
        ),
    ]
