# Generated by Django 3.1.3 on 2020-11-29 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0005_auto_20201129_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
