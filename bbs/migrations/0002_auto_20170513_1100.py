# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='head_img',
            field=models.ImageField(default=0, upload_to='', verbose_name='文章标题图片'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='priority',
            field=models.IntegerField(default=0, null=True, verbose_name='优先级'),
        ),
    ]
