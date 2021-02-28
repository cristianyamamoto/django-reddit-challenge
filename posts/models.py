from django.db import models
from helpers.models import TimestampModel
from topics.models import Topic


class Post(TimestampModel):
    title = models.CharField(max_length=128, blank=False)
    content = models.TextField(blank=True)
    topic = models.ForeignKey(
        Topic, related_name='topic',
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['updated_at']

    # Shows up in the admin list
    def __str__(self):
        return self.title

