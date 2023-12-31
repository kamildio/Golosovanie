from django.db import models

class CanditeForm(models.Model):
    candidate = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True)
    first_name = models.TextField(max_length=75, blank=True)
    last_name = models.TextField(max_length=75, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default=' ')
    partiya = models.TextField(max_length=75, blank=True)

    class Meta:
        verbose_name = 'Форма Кандидата'
        verbose_name_plural = 'Формы Кандидатов'

    def __str__(self):
        return self.first_name