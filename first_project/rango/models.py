from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Lategory(models.Model):
    name = models.CharField(max_length=128,unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    def save(self,*args,**kwargs):
        self.slug =slugify(self.name)
        super(Lategory,self).save(*args,**kwargs)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Lategory)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profiles_images', blank=True)

    def __unicode__(self):
        return self.user.username
