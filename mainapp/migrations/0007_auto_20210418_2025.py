# Generated by Django 3.1.7 on 2021-04-18 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210418_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='number',
            name='materials',
        ),
        migrations.AddField(
            model_name='category',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.material', verbose_name='Материал к категории задания'),
        ),
    ]