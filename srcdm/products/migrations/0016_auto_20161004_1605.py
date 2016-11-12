# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20161004_0519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thumbnail',
            old_name='products',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='height',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='media',
            field=models.ImageField(height_field=b'height', width_field=b'width', null=True, upload_to=products.models.thumbnail_location, blank=True),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='width',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
