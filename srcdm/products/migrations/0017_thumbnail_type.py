# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20161004_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='type',
            field=models.CharField(default=b'hd', max_length=20, choices=[(b'hd', b'HD'), (b'sd', b'SD'), (b'micro', b'Micro')]),
        ),
    ]
