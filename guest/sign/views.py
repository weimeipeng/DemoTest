from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password")
        if(username == "admin" and password =="123456"):
            response = HttpResponseRedirect("/event_manage/")
            #response.set_cookie('uname',username,3600)
            request.session['uname']=username
            return response

        else:
           # return HttpResponse("用户名或密码错误，请重新输入！！！")
           return render(request,"login.html",{'error':'用户名或密码错误！！！'})

def event_manage(request):
    #uname = request.COOKIES.get('uname','')
    uname = request.session.get('uname','')
    return render(request,"event_manage.html",{"uname":uname})