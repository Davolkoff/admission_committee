# Generated by Django 4.0.2 on 2023-06-19 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_menubuttons_redirection_page_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('window_number', models.IntegerField(verbose_name='Номер окна')),
                ('current_ticket', models.IntegerField(blank=True, null=True, verbose_name='Текущий посетитель')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.IntegerField(verbose_name='Номер талона')),
                ('question', models.CharField(max_length=60, verbose_name='Вопрос')),
            ],
        ),
        migrations.AlterField(
            model_name='menubuttons',
            name='redirect_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirect_page', to='core.pages', verbose_name='Страница переадресации'),
        ),
    ]
