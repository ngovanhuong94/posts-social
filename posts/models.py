from django.db import models
from django.conf import settings
from django.utils.text import slugify 


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts_created')
	title = models.CharField(max_length=200, unique=True)
	text = models.TextField()

	slug = models.SlugField(max_length=200, blank=True)
	users_liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='posts_liked', blank=True)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)	


