from django.shortcuts import render,redirect
from fs.models import userdetail,subdetail
import datetime as dt
# Create your views here.
def index(request):
    request.session['usr']=""
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        if userdetail.objects.filter(email=request.POST['your-email']).exists():
            return redirect('fs:signup')
        else:
            userdetail(email=request.POST['your-email'],name=request.POST['full-name'],password=request.POST['password']).save()
            subdetail(email=request.POST['your-email'],sub="0",date="0000-00-00").save()
            return redirect('fs:login')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        if (request.POST['inputEmail']=='admin@gmail.com' and request.POST['inputPassword']=='@1geniUs'):
            print('YSE')
            request.session['usr']='admin'
            return redirect('fs:admindash')
        elif userdetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():

            request.session['usr']=request.POST['inputEmail']
            return redirect('fs:dashboard')
        else:
            print('NO')
            return redirect('fs:login')
    return render(request,'login.html')

def logout(request):
    request.session['usr']=""
    return render(request,'index.html')

def dashboard(request):
    if request.session['usr']:
        return render(request,'dashboard.html')
    else:
        return redirect('fs:login')

def admindash(request):
    if (request.session['usr'] and request.session['usr']=='admin'):
        return render(request,'admin.html')
    else:
        return redirect('fs:login')

def subscription(request):
    if request.session['usr']:
        if request.method=="POST":
            daa=str(dt.datetime.fromisoformat(str(dt.datetime.now()).split(' ')[0])+dt.timedelta(days=365)).split(' ')[0]
            subdetail.objects.filter(email=request.session['usr']).update(date=daa,sub="1")
            return redirect('fs:subscription')
        a=subdetail.objects.filter(email=request.session['usr'])
        if a[0].sub=="0":
            return render(request,'subscription.html')
        #     return render(request,'subscription.html')
        else:
            return render(request,'subscription.html',{'sub':a[0]})
    else:
        return redirect('fs:login')
