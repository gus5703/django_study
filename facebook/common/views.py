from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.contrib.auth import login as auth_login
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            print(user, user.is_active)
            auth_login(request,user)

    return render(request, 'login.html')



def logout(request):
    auth_login(request)
    return redirect('/login/')

