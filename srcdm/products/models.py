from django.conf import settings

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.core.files.storage import FileSystemStorage





def download_media_location(instance, filename):
	return '%s/%s' %(instance.slug, filename)


class Product(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	managers = models.ManyToManyField(settings.AUTH_USER_MODEL,
			related_name='managers_model', blank=True)
	media = models.FileField(null=True, blank=True,
			upload_to=download_media_location,
			storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
	title = models.CharField(max_length=120)
	slug = models.SlugField(blank=True, unique=True)
	description = models.TextField()
	price = models.DecimalField(max_digits=100,
			decimal_places=2, default=9.99, null=True, blank=True)
	sale_price = models.DecimalField(max_digits=100,
			decimal_places=2, default=6.99, null=True, blank=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-id']	


	def get_absolute_url(self):
		view_name = 'products:detail_slug'
		return reverse(view_name, kwargs={'slug':self.slug})

	def get_download(self):
		view_name = 'products:download_slug'
		url = reverse(view_name, kwargs={'slug':self.slug})
		return url
		
		


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Product.objects.filter(slug=slug)
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)

	return slug


def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)	




def thumbnail_location(instance, filename):
	return '%s/%s' %(instance.product.slug, filename)



THUMB_CHOICES = (
	("hd", "HD"),
	("sd", "SD"),
	("micro", "Micro"),
	)
	


class Thumbnail(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	product = models.ForeignKey(Product)
	type = models.CharField(max_length=20, choices=THUMB_CHOICES, default='hd')
	height = models.CharField(max_length=20, null=True, blank=True)
	width = models.CharField(max_length=20, null=True, blank=True)

	media = models.ImageField(null=True, blank=True,
			height_field='height',
			width_field='width',
			upload_to=thumbnail_location,
			)


	def __unicode__(self):
		return (self.media.path)


import os
import shutil
from PIL import Image

from django.core.files import File

def product_post_save_receiver(sender, instance, created, *args, **kwargs):
	if instance.media:
		hd = Thumbnail.objects.get_or_create(product=instance, type='hd')[0]
		sd = Thumbnail.objects.get_or_create(product=instance, type='sd')[0]
		micro = Thumbnail.objects.get_or_create(product=instance, type='micro')[0]

		hd_max = (400, 400)
		sd_max = (200, 200)
		micro_max = (50, 50)

		filename = os.path.basename(instance.media.path)

post_save.connect(product_post_save_receiver, sender=Product)	


class MyProducts(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)

	products = models.ManyToManyField(Product, blank=True)

	def __unicode__(self):
		return '%s' %(self.products.count())

	class Meta:
		verbose_name = 'My Products'
		verbose_name_plural = 'My Products'
		