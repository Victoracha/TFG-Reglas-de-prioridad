

# Create your models here.
from django.db import models
"""from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())"""


class Pieza(models.Model):
    nPieza = models.DateTimeField(auto_now_add=True)
    """class Meta:
        ordering = ('created',)"""
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Pieza.objects.create(**validated_data)
