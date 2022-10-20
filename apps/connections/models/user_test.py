from django.db import models


class UserTest(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True)
    test_id = models.ForeignKey("tests.Test", on_delete=models.CASCADE, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    start_time = models.TimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)
