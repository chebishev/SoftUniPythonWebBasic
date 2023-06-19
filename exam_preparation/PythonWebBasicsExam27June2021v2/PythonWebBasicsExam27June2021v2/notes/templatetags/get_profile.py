from django import template

from PythonWebBasicsExam27June2021v2.notes.models import Profile

register = template.Library()


@register.simple_tag
def check_profile():
    return Profile.objects.first()
