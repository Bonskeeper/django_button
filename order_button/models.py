from django.db import models


class ButtonResponse(models.Model):
    status_code = models.CharField(max_length=100)
    response_answer = models.TextField()
    response_date = models.DateTimeField()
