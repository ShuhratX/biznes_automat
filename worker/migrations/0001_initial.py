# Generated by Django 3.1.2 on 2021-06-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='Ismi')),
                ('last_name', models.CharField(max_length=40, verbose_name='Familiyasi')),
                ('salary', models.PositiveIntegerField(verbose_name='Maoshi')),
            ],
        ),
    ]