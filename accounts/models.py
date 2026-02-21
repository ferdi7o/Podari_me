from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        validators= [
            MinLengthValidator(
                4,
                message='Името трябва да съдържа поне 4 символа!'
            ),
            RegexValidator(
                regex='^[A-Za-z]+$',
                message='Името трябва да съдържа само букви!'
            )
        ]
    )

    last_name = models.CharField(
        max_length=20,
        validators= [ # This validation used two time, it can create a file validator.py and with 1 function called from here!
            MinLengthValidator(
                4,
                message='Фамилното име трябва да съдържа поне 4 символа!'
                               ),
            RegexValidator(
                regex='^[A-Za-z]+$',
                message='Името трябва да съдържа само букви!'
            )
        ]
    )
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True) # the pictures will come from the internet

    def __str__(self):
        return f"{self.first_name} {self.last_name}"