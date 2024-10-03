from django.shortcuts import render
from blog.forms import UserForm, LoginForm, AddPostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from blog.models import Post
from django.contrib.auth.models import Group

# home view
def home_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

# About view
def About_view(request):
    return render(request, 'blog/about.html')

# Contact view
def contact_view(request):
    return render(request, 'blog/contact.html')

# Dashboar view
def dashboard_view(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        groups = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts':posts, 'full_name': full_name, 'groups':groups})
    else:
        return redirect('/login/')

# signup view
def signup_view(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            messages.success(request, 'congratulation! You have become an author.')
            user = form.save()
            group = Group.objects.filter(name='Author').first()
            if group:
                user.groups.add(group)
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form':form})

# login view
def login_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return redirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return redirect('/dashboard/')
    
# logout view
def logout_view(request):
    logout(request)
    return redirect('/')

# Add new post 
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post_data = Post(title=title, desc=desc)
                post_data.save()
                form = AddPostForm()
        else:
            form = AddPostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return redirect('/login/')
    
# Add new post 
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            post_obj = Post.objects.filter(id=id).first()
            form = AddPostForm(request.POST, instance=post_obj)
            if form.is_valid():
                form.save()
        else:
            post_obj = Post.objects.filter(id=id).first()
            form = AddPostForm(instance=post_obj)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return redirect('/login/')

# Add new post 
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            post_obj = Post.objects.filter(id=id).first()
            post_obj.delete()
            return redirect('/dashboard/')
    else:
        return redirect('/login/')
