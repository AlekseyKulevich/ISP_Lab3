from django.db import models
from enumfields import EnumField
import datetime
from taskManager.enumTasks import Priority, Status
from django.contrib.auth.models import User


class Task(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    title = models.CharField('Title', max_length=100)
    pub_date = datetime.datetime.now()
    finish = models.DateTimeField(null=True)
    priority = EnumField(Priority)
    status = EnumField(Status)
    information = models.TextField('Information')
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    id = models.CharField(max_length=64, primary_key=True)
    friends = models.ManyToManyField('UserProfile', blank=True)

    def __str__(self):
        return self.id
