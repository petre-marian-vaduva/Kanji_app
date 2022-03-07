from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Kanji(models.Model):
    character = models.CharField(max_length=20)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_number = models.BooleanField()
    is_radical = models.BooleanField()

    def __str__(self):
        return u'%s %s %s %s' % (self.character, self.level, self.is_number, self.is_radical)

    class Meta:
        verbose_name_plural = 'Kanji'

class Portuguese(models.Model):
    character = models.ForeignKey(Kanji, on_delete=models.CASCADE)
    meaning = models.CharField(max_length=50, null=True)
    example = models.TextField()

    def __str__(self):
        return u'%s %s' % (self.meaning, self.example)

    class Meta:
        verbose_name_plural = 'Portuguese'
