# Generated by Django 4.2.5 on 2023-10-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia_prima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('u_medida', models.CharField(max_length=5, verbose_name='Un. Medida')),
                ('preco', models.FloatField(max_length=4, verbose_name='Preço')),
            ],
        ),
    ]
