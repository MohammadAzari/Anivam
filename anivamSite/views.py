from django.shortcuts import render

def home(request):
    return render(request, 'anivamSite/index.html')

def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
    # following = None
    # followers = None
    # credit = None
    # # if request.user.is_authenticated:
    #     followers_numb = len(request.user.followers.all())
    #     followings_numb = len(request.user.followings.all())
    #     credit = request.user.credit
    # {'following':followers_numb, 'followings':followings_numb, 'credit':credit}
    return render(request, 'anivamSite/profile.html', {'username':username})