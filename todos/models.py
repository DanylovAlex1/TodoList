from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Board {}, created at{}'.format(self.title, self.created)


class TodoList(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    board = models.ForeignKey(Board, verbose_name='Board', on_delete=models.PROTECT)

    def __str__(self):
        return 'TodoList {}, created at{}'.format(self.title, self.created)