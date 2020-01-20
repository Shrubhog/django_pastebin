import uuid
from django.db import models

class Paste(models.Model):
    text = models.TextField(default="")
    title = models.CharField(max_length=15, default="Paste")
    pub_date = models.DateTimeField('date published')
    pub_user = models.CharField('username', max_length=30, default="Guest")

    paste_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.title}"
    