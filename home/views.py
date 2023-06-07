from django.shortcuts import render, redirect
from .form import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.views import View
from django.urls import reverse
from blog.models import Post
from django.utils import timezone
from datetime import datetime


# Create your views here.

# home
def index(request):
        data = Post.objects.all()
        return render(request, 'page/home.html', {'data': data,});

# contact
def contact(request):
        return render(request, 'page/contact.html');

# register
def register(request):
        form = RegisterForm()
        if request.method == 'POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/login')
        return render(request, 'page/register.html', {'form': form})

# login via facebook
class FacebookLogin(View):
    def get(self, request):
        provider_login_url = reverse('socialaccount_login', args=['facebook'])
        return redirect(provider_login_url)

# logout
def logout_view(request):
    logout(request)
    return redirect('/')
