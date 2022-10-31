from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class HumanType(models.Model):
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)


class LanguageChoices(models.Model):
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)


class User(models.Model):

    full_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=12, validators=[phone_regex], blank=True, null=True, default=None)
    language = models.ForeignKey(LanguageChoices, on_delete=models.CASCADE, blank=True, null=True, default=None)
    balance = models.DecimalField(max_digits=11, decimal_places=4, default=0, null=True, blank=True)

    invited_users = models.CharField(max_length=150, blank=True, null=True, default=None)
    human_type = models.ForeignKey("users.HumanType", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.full_name)


