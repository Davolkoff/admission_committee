# Generated by Django 4.0.2 on 2023-06-19 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_operators_current_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operators',
            name='current_ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.tickets', verbose_name='Текущий посетитель'),
        ),
    ]