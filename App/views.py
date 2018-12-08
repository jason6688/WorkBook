from django.shortcuts import render,redirect

# from django.http import HttpResponse
import hashlib

from . import models


# Create your views here.
def home(request):
    # return HttpResponse("<h1>Welcome You~</h1>")
    pwd = hashlib.md5(b'123456').hexdigest()
    # print(pwd)
    # users = models.User.objects.all()
    # for user in users:
    # print(user.user_name)

    # user = models.User.objects.get(user_name='admin')
    # user = models.User.objects.filter(user_name='admin').first()
    user = models.User.objects.filter(user_name='admin', user_pwd=pwd).get()
    print(user.user_name)

    return render(request, 'home.html', {'user': user})

def login(request):
    return render(request, 'login.html')

def login_check(request):
    user_name = request.POST.get('user_name')
    user_pwd = request.POST.get('user_pwd')
    md5 = hashlib.md5()
    md5.update(user_pwd.encode('utf-8'))
    user_pwd = md5.hexdigest()
    #user_pwd = hashlib.md5().update(user_pwd.encode('utf-8')).hexdigest()
    #user = models.User.objects.filter(user_name=user_name, user_pwd=user_pwd).get()  #get方法查询不到结果会报异常
    user_count = models.User.objects.filter(user_name=user_name, user_pwd=user_pwd).count()
    #print(user)
    #print(user_pwd)
    if user_count == 0:
        return redirect('/login/')
    else:
        return redirect('/home/')

