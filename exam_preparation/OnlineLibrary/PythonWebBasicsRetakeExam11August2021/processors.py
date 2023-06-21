from PythonWebBasicsRetakeExam11August2021.online_library.models import Profile


def get_profile(request):
    profile = Profile.objects.first()
    return {'profile': profile}
