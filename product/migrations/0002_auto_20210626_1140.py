# Generated by Django 3.1.2 on 2021-06-26 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='variation',
            field=models.CharField(choices=[('debit', 'Debitor'), ('kredit', 'Kreditor')], default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.partner', verbose_name='Hamkor'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.worker', verbose_name='Ishchi'),
        ),
    ]
