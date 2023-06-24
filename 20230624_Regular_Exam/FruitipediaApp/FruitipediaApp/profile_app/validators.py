from django.core.exceptions import ValidationError


def name_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")
