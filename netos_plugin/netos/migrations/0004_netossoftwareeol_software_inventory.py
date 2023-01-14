# Generated by Django 4.0.8 on 2022-11-30 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netos', '0003_netossoftwareeol'),
    ]

    operations = [
        migrations.AddField(
            model_name='netossoftwareeol',
            name='software_inventory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='software_eol', to='netos.netossoftwareinventory'),
            preserve_default=False,
        ),
    ]
