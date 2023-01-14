# Generated by Django 4.0.8 on 2022-12-15 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netos', '0004_netossoftwareeol_software_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='bulletin',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='end_of_routine_failure_analysis_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='end_of_service_contract_renewal_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='hardware_inventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hardware_eol', to='netos.netoshardwareinventory'),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='last_day_for_service_contract',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='last_day_of_support_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='last_sale_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='maintenance_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='migration_info',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='migration_option',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='migration_product_id',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='migration_product_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='migration_strategy',
            field=models.CharField(blank=True, max_length=1334, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='product_id',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='product_id_description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='product_migration_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='record_update_timestamp',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='vulnerability_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]