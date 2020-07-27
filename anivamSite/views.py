from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Person
from django.contrib.auth.models import User

def home(request):
    return render(request, 'anivamSite/index.html')

@login_required
def profile_base(request):
    user_url = request.user.username + '/' 
    return redirect(user_url)

@login_required
def profile(request, username):
    user = request.user.username
    its_me = None
    is_follow = None
    if user == username:
        its_me = False
    else:
        its_me = True

    user_check = User.objects.filter(username=username)
    if len(user_check) == 0:
        return HttpResponse("User not found!")
    else:
        u = user_check[0]
        person = Person.objects.get(user=u)

        p = Person.objects.get(user=request.user)

        if person in p.followers.all():
            is_follow = True
        else:
            is_follow = False
        
        if request.method == 'POST':
            key = request.POST.get('key')
            if key == "want_unfollow":
                p.followers.remove(person)
                person.followings.remove(p)
            elif key == "want_follow":
                p.followers.add(person)
                person.followings.add(p)
                
        content = {
            'username':username,
            'its_me':its_me,
            "person":person,
            'is_follow':is_follow,
            'following':len(person.followings.all())
        }
        return render(request, 'anivamSite/profile.html', content)