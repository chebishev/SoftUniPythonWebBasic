from django.core.exceptions import ValidationError


def name_validator(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")
