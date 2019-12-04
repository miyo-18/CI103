from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from accounts.forms import RegistrationForm
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
def homepage(request):
    return render(request, 'accounts/home.html') #takes up to 3 parameters - request, template name, context

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect("accounts:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'accounts/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

def post(request):
    return render(request, 'accounts/post.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("accounts:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {{username}}")
                return redirect("accounts:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form":form})
