# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.FileField(null=True, upload_to=django.core.files.storage.FileSystemStorage(b'/home/sudhamsu/Desktop/dm/static_cdn/protected'), blank=True),
        ),
    ]
