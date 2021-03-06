# Generated by Django 2.2.6 on 2019-12-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191216_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('start', models.TimeField(verbose_name='Horário')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('speakers', models.ManyToManyField(to='core.Speaker', verbose_name='Palestrante(s)')),
            ],
            options={
                'verbose_name': 'palestra',
                'verbose_name_plural': 'palestras',
            },
        ),
    ]
