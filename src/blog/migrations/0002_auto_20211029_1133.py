# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-29 11:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=2000, null=True),
        ),
    ]
