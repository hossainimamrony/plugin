# Generated by Django 4.0.8 on 2022-12-15 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netos', '0005_alter_netoshardwareeol_bulletin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netoshardwareeol',
            name='product_id',
            field=models.CharField(default=1, max_length=48),
            preserve_default=False,
        ),
    ]