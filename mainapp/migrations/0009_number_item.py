# Generated by Django 3.1.7 on 2021-04-20 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210420_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.item'),
        ),
    ]
