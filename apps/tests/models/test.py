from django.db import models


class TestPicture(models.Model):
    image = models.ImageField(upload_to='test_pictures')

    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['-id']


class Classes(models.Model):
    title = models.CharField(max_length=45, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)


class Themes(models.Model):
    name = models.CharField(max_length=150, blank=True)
    class_id = models.ForeignKey("tests.Classes", on_delete=models.CASCADE, null=True, blank=True)
    science_id = models.ForeignKey("books.Science", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.name)


class TestType(models.Model):
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)


class Test(models.Model):
    name = models.CharField(max_length=150, blank=True)
    question = models.TextField(blank=True)
    is_visible = models.BooleanField(default=True)
    admin_id = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True)
    picture_id = models.ForeignKey("tests.TestPicture", on_delete=models.CASCADE, null=True, blank=True)
    language_id = models.ForeignKey("users.LanguageChoices", on_delete=models.CASCADE, null=True, blank=True)
    theme_id = models.ForeignKey("tests.Themes", on_delete=models.CASCADE, null=True, blank=True)

    for_person_id = models.ForeignKey("users.HumanType", on_delete=models.CASCADE, null=True, blank=True)
    test_type = models.ForeignKey("tests.TestType", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.name)
