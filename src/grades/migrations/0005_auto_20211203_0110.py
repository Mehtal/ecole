# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-12-03 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0004_auto_20211203_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='level',
            field=models.CharField(choices=[('الإبتدائي', 'الإبتدائي'), ('المتوسط', 'المتوسط'), ('الثانوي', 'الثانوي')], max_length=30),
        ),
    ]
