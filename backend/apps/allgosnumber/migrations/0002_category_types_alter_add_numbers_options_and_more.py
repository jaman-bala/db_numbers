# Generated by Django 4.1.3 on 2023-12-19 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allgosnumber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Типы')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'типы',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.AlterModelOptions(
            name='add_numbers',
            options={'ordering': ['-created'], 'verbose_name': 'Добовления номеров в базу', 'verbose_name_plural': 'Общая база номеров'},
        ),
        migrations.AlterModelOptions(
            name='category_number',
            options={'verbose_name': 'номера ', 'verbose_name_plural': 'Региональный номер'},
        ),
        migrations.AlterModelOptions(
            name='category_unaa',
            options={'verbose_name': 'подраздиления', 'verbose_name_plural': 'Подраздиление УНАА'},
        ),
        migrations.RemoveField(
            model_name='add_numbers',
            name='category_region',
        ),
        migrations.RemoveField(
            model_name='add_numbers',
            name='title',
        ),
        migrations.RemoveField(
            model_name='category_number',
            name='numbers',
        ),
        migrations.RemoveField(
            model_name='category_unaa',
            name='units',
        ),
        migrations.AddField(
            model_name='add_numbers',
            name='application',
            field=models.CharField(default=213, max_length=50, verbose_name='Номер заявки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_numbers',
            name='number',
            field=models.CharField(default=321, max_length=50, verbose_name='Гос номер'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category_number',
            name='title',
            field=models.CharField(default=2312, max_length=50, unique=True, verbose_name='Номера'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category_unaa',
            name='title',
            field=models.CharField(default=1, max_length=50, unique=True, verbose_name='Наименование отделов'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='add_numbers',
            name='category_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allgosnumber.category_number', verbose_name='Гос номер'),
        ),
        migrations.AlterField(
            model_name='add_numbers',
            name='category_unaa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allgosnumber.category_unaa', verbose_name='Отделение'),
        ),
        migrations.DeleteModel(
            name='Category_Region',
        ),
        migrations.AddField(
            model_name='add_numbers',
            name='category_types',
            field=models.ForeignKey(default=3213, on_delete=django.db.models.deletion.CASCADE, to='allgosnumber.category_types', verbose_name='Типы'),
            preserve_default=False,
        ),
    ]
