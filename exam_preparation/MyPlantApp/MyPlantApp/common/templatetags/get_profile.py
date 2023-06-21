from django import template
from MyPlantApp.profile_app.models import Profile

register = template.Library()


@register.simple_tag
def check_profile():
    return Profile.objects.first()
