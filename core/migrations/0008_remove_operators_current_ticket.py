# Generated by Django 4.0.2 on 2023-06-19 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_operators_current_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operators',
            name='current_ticket',
        ),
    ]
