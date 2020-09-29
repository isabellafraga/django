# Generated by Django 3.0.3 on 2020-09-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_remove_dadosform_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('sobrenome', models.CharField(max_length=256)),
                ('telefone', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('duracao', models.PositiveIntegerField()),
                ('ano_lancamento', models.PositiveIntegerField()),
            ],
        ),
    ]
