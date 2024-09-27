from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='/login-user/')
def Index(request):
    news = News.objects.all().order_by('-created_at')
    profiles = Zink_user.objects.all().order_by('-created_at')
    posts = Post.objects.all().order_by('-created_at')

    params = {'profiles' : profiles, 'news' : news,'posts' : posts}
    return render(request, 'index.html', params)


@login_required(login_url='/login-user/')
def Friends(request):
    news = News.objects.all().order_by('-created_at')
    profiles = Zink_user.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    
    params = {'profiles' : profiles, 'news' : news,'posts' : posts}
    return render(request, 'friends.html',params)


@login_required(login_url='/login-user/')
def Messages(request):
    news = News.objects.all().order_by('-created_at')
    profiles = Zink_user.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        chat = request.POST.get('message')
        user_chat = Chat.objects.create(
            chat=chat,
        )
        user_chat.save()

    messages = Chat.objects.all()

    params = {'profiles' : profiles, 'news' : news,'posts' : posts , 'messages' : messages}
    return render(request, 'messages.html',params)


@login_required(login_url='/login-user/')
def Settings_page(request):
    news = News.objects.all().order_by('-created_at')
    profiles = Zink_user.objects.all()
    posts = Post.objects.all().order_by('-created_at')

    params = {'profiles' : profiles, 'news' : news,'posts' : posts}
    return render(request, 'settings.html',params)

@login_required(login_url='/login-user/')
def profile_view(request):
    if request.method == 'POST':
        profile_img = request.FILES.get('profile_img')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        profile_bio = request.POST.get('profile_bio')
        profile_link = request.POST.get('profile_link')

        user = Zink_user.objects.create(
            profile_img = profile_img,
            first_name = first_name,
            last_name = last_name,
            username = username,
            profile_bio = profile_bio,
            profile_link = profile_link,
        )
        user.save()
    news = News.objects.all().order_by('-created_at')
    profiles = Zink_user.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    
    params = {'profiles' : profiles, 'news' : news,'posts' : posts}
    return render(request, 'profile.html', params)

@login_required(login_url='/login-user/')
def Add_news(request):
    profiles = Zink_user.objects.all()
    if request.method == 'POST':
        heading = request.POST.get('heading')
        sub_heading = request.POST.get('sub_heading')
        news = request.POST.get('news')

        new_add = News.objects.create(
            heading = heading,
            sub_heading = sub_heading,
            news  = news,
        )
        new_add.save()

    news = News.objects.all().order_by('-created_at')
    posts = Post.objects.all().order_by('-created_at')
    params = {'profiles' : profiles, 'news' : news,'posts' : posts}
    return render(request, 'add_news.html', params)

@login_required(login_url='/login-user/')
def Add_post(request):
    news = News.objects.all().order_by('-created_at')
    profiles = Zink_user.objects.all()
    if request.method == 'POST':
        post = request.FILES.get('post')
        fullname = request.POST.get('fullname')

        add_post = Post.objects.create(
            post = post,
            fullname = fullname,
        )
        add_post.save()
    posts = Post.objects.all().order_by('-created_at')
    params = {'profiles' : profiles, 'news' : news,'posts' : posts}
    return render(request, 'add_post.html', params)