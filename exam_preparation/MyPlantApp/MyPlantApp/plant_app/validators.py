from django.core.exceptions import ValidationError


def name_is_alpha(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")
