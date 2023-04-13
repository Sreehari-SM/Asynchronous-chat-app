from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'accounts_profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ('name',)
