# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import products.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0014_myproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('height', models.CharField(max_length=20)),
                ('width', models.CharField(max_length=20)),
                ('media', models.ImageField(height_field=b'height', width_field=b'width', null=True, upload_to=products.models.download_media_location, blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='myproducts',
            options={'verbose_name': 'My Products', 'verbose_name_plural': 'My Products'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='products',
            field=models.ForeignKey(to='products.Product'),
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
