# Generated by Django 4.1.3 on 2023-12-15 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allgosnumber', '0009_alter_add_numbers_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_numbers',
            name='category_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allgosnumber.category_number', verbose_name='Гос номер'),
        ),
        migrations.AlterField(
            model_name='add_numbers',
            name='category_types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allgosnumber.category_types', verbose_name='Типы'),
        ),
        migrations.AlterField(
            model_name='add_numbers',
            name='category_unaa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allgosnumber.category_unaa', verbose_name='Отделение'),
        ),
    ]
