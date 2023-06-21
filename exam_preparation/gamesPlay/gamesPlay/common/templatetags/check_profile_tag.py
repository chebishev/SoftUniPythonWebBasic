from gamesPlay.profile_app.models import ProfileModel
from django import template

register = template.Library()


@register.simple_tag
def get_profile():
    return ProfileModel.objects.first()
