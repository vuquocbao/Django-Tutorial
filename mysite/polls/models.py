import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # Holds question string
    pub_date = models.DateTimeField('date published') # Holds date question was published

    # Converts representation of object as string
    def __str__(self):
        return self.question_text

    # Return boolean if question recently published
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question) # Link choice to question model
    choice_text = models.CharField(max_length=200) # Holds choice string
    votes = models.IntegerField(default=0) # Integer to count votes

    # Converts representation of object as string
    def __str__(self):
        return self.choice_text