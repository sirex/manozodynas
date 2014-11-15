from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render

from manozodynas.apps.users.forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None and user.is_active:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'manozodynas/users/login.html', {'form': form})
