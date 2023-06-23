from PythonWebBasicsRetakeExam19April2022.profile_app.models import Profile


def get_profile(request):
    profile = Profile.objects.first()
    return {'profile': profile}
