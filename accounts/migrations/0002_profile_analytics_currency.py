# Generated by Django 3.1.4 on 2020-12-27 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='analytics_currency',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='stock.currency'),
        ),
    ]