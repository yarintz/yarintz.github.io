from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

class Todo(models.Model):
    title = models.CharField(max_length=256)
    user =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    copleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo:todo_detail', kwargs={'pk': self.pk})