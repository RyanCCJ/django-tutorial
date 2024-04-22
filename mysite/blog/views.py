from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from blog import models, forms

def hello_world(request):
    time = datetime.now()
    return render(request, 'hello_world.html', locals())

def post(request):
    posts = models.Post.objects.all()
    time = datetime.now()
    return render(request, 'post.html', locals())

def index(request):
    username = user_login(request)
    posts = models.Post.objects.all()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    username = user_login(request)
    posts = models.Post.objects.all()
    try:
        post = models.Post.objects.get(slug=slug)   
        
        if post != None:
            comments = models.Comment.objects.filter(post=post)
            
            try:
                user_id = request.POST['user_id']
                user_pass = request.POST['user_pass']
                user_comment = request.POST['user_comment']        
                user = models.User.objects.get(nickname=user_id)             
                
                if user.password == user_pass:     
                    comment = models.Comment.objects.create(author=user, post=post, content=user_comment)
                    comment.save()       
                    message = "儲存成功！"

            except:
                message = "請正確填寫每一個欄位"

            return render(request, 'post.html', locals())
    except:
        return redirect('/')

def user(request):
    username = user_login(request)
    posts = models.Post.objects.filter(author__name=username)

    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            message = '儲存成功！'
        else:
            message = '儲存失敗，請正確填寫每一個欄位'
    else:
        post_form = forms.PostForm()
        message = '請正確填寫每一個欄位'
    
    return render(request, 'user.html', locals())

def login(request):
    posts = models.Post.objects.all()
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_pass = request.POST['password']
            try:
                user = models.User.objects.get(name = login_name)
                if user.password == login_pass:
                    request.session['user_name'] = user.name #<--注意這行！
                    messages.add_message(request, messages.SUCCESS, ('登入成功！歡迎：'+user.nickname))
                    return redirect('/')
                else:
                    message = '密碼錯誤，請再檢查一次'
            except:
                message = '找不到使用者'
        else:
            message = '請正確填寫每一個欄位'
    else:
        login_form = forms.LoginForm()    
    return render(request, 'login.html', locals())

def logout(request):
    if 'user_name' in request.session:
        Session.objects.all().delete()
        messages.add_message(request, messages.SUCCESS, '登出成功！')
    return redirect('/')

def user_login(request):
    username = ''
    if 'user_name' in request.session:
        username = request.session['user_name']
    return username
