from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from pyexpat.errors import messages

from accounts.models import Profile


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Gift(models.Model):
    TYPE_CHOICES = [
        ('Електроника', 'Електроника'),
        ('Дом. Потреби', 'Домашни Потреби'),
        ('Животни', 'Животни'),
        ('Други', 'Други'),
    ]

    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(10, message='Заглавието трябва да съдържа поне 10 символа!'),
            RegexValidator(
                regex='^[A-Za-z0-9_ ]+$',
                message= 'Заглавието трябва да съдържа само букви и цифри'
            )
        ],
    )

    description = models.TextField(
        max_length=400,
        validators=[MinLengthValidator(20, message='Описанието трябва да съдържа поне 20 символа!')]
    )
    category = models.CharField(max_length=30, choices=TYPE_CHOICES)
    image_url = models.URLField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='gifts')
    tags = models.ManyToManyField(Tag, blank=True)
    status_gift = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title