from django.db import models

# Create your models here.

class Comment(models.Model):
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    upated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'commenthh'