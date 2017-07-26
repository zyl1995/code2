import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_data = models.DateTimeField('data published')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.publish_data >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'publish_data'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    pass


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text

    pass

# Create your models here.
