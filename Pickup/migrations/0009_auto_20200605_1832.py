# Generated by Django 3.0.7 on 2020-06-05 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pickup', '0008_auto_20200605_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pickup',
            old_name='odoMeter',
            new_name='odoMeter1',
        ),
    ]