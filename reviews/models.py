from django.db import models
from django.contrib.auth.models import User

from django.db.models import Avg

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Anonymous')

    def average_rating(self):
        return self.review_set.aggregate(Avg('rating'))['rating__avg']

    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING,)

    pub_date = models.DateTimeField('date published')
    user_name = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE) 
    # user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
