from PythonWebBasicsExam27February2022.profile_app.models import Profile


# this code will be automatically added in all view's context in order to keep the code DRY
# the function will be active only if you add it in settings.py -> TEMPLATES -> OPTIONS
def get_profile(request):
    profile = Profile.objects.first()
    return {'profile': profile}
