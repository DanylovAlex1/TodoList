from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from reminder.tasks import append_task


class Reminder(models.Model):
    email = models.EmailField(verbose_name='')
    text = models.TextField(verbose_name='Text', max_length=400)
    delay = models.IntegerField('Delay', default=10)
    duetime = models.DateTimeField(verbose_name='Due time', default=datetime.now, blank=True)

    def __str__(self):
        return 'Remind to {}, if overdue more than {} minutes'.format(self.email, self.delay)


@receiver(post_save, sender=Reminder)
def reminder_post_save(sender, instance, *args, **kwargs):
    append_task(instance.email, instance.text, instance.delay, instance.duetime)
