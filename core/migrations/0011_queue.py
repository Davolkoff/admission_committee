# Generated by Django 4.2.1 on 2023-06-19 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_operators_current_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('window_number', models.IntegerField(verbose_name='Номер окна')),
                ('current_ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.tickets', verbose_name='Текущий посетитель')),
            ],
        ),
    ]
