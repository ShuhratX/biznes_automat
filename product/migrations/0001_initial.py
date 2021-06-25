# Generated by Django 3.1.2 on 2021-06-25 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ismi')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon raqami')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('price', models.PositiveIntegerField(verbose_name='Narxi')),
                ('count', models.PositiveIntegerField(verbose_name='Soni')),
                ('description', models.TextField(verbose_name='Tafsilot')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='Ismi')),
                ('last_name', models.CharField(max_length=40, verbose_name='Familiyasi')),
                ('salary', models.PositiveIntegerField(verbose_name='Maoshi')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Soni')),
                ('paid', models.BooleanField(default=False, verbose_name="To'langan")),
                ('summa', models.PositiveIntegerField(verbose_name='Summa')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.partner', verbose_name='Hamkor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Maxsulot')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.CharField(max_length=255, verbose_name='Asos')),
                ('summa', models.PositiveIntegerField(verbose_name='Summa')),
                ('closed', models.BooleanField(default=False, verbose_name='Yopilgan')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.partner', verbose_name='Hamkor')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.PositiveIntegerField(verbose_name='Summa')),
                ('base', models.CharField(max_length=255, verbose_name='Asos')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.partner', verbose_name='Hamkor')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.worker', verbose_name='Ishchi')),
            ],
        ),
    ]