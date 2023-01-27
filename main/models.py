from django.core.validators import RegexValidator
from django.db import models


class Link(models.Model):
    url = models.URLField(max_length=2048)
    token = models.CharField(max_length=6, unique=True, validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9]{6}$',
            code='invalid_token',
            message='Token can only contain alphabets and numerals',
        ),
    ])
    clicks_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
