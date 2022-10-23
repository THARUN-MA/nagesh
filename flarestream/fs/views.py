from django.shortcuts import render,redirect
from fs.models import userdetail,subdetail,albcounter,srtmvcounter,album,short
import datetime as dt
import qrcode
import qrcode.image.svg
from io import BytesIO
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

def albumsong(request):
    if request.session['usr']:
        data=album.objects.all()
        return render(request,'albumsong.html',{'data':data})
    else:
        return redirect('fs:login')

def shortmovie(request):
    if request.session['usr']:
        data=short.objects.all()
        return render(request,'shortmovie.html',{'data':data})
    else:
        return redirect('fs:login')

def addmedia(request):
    if (request.session['usr'] and request.session['usr']=='admin'):
        if request.method=="POST":

            if request.FILES['myfile']:
                if request.POST['opt']=="short":
                    if short.objects.filter(name=request.FILES['myfile'].name).exists():
                        return redirect('fs:addmedia')
                    else:
                        iidd=srtmvcounter.objects.all()
                        short(name=request.FILES['myfile'].name,filesall=request.FILES['myfile'],sid=iidd[0].sid,title=request.POST['title'],upiid=request.POST['upiid'],desc=request.POST['desc']).save()
                        srtmvcounter.objects.filter(sid=iidd[0].sid).update(sid=str(int(iidd[0].sid)+1))
                        print('Successful srt')
                        return redirect('fs:admindash')
                elif request.POST['opt']=="album":
                    if album.objects.filter(name=request.FILES['myfile'].name).exists():
                        return redirect('fs:addmedia')
                    else:
                        iidd=albcounter.objects.all()
                        album(name=request.FILES['myfile'].name,filesall=request.FILES['myfile'],aid=iidd[0].aid,title=request.POST['title'],upiid=request.POST['upiid'],desc=request.POST['desc']).save()
                        albcounter.objects.filter(aid=iidd[0].aid).update(aid=str(int(iidd[0].aid)+1))
                        print('Successful alb')
                        return redirect('fs:admindash')

        return render(request,'addmedia.html')
    else:
        return redirect('fs:login')


def watchshort(request,value=None):
    if request.session['usr']:
        a=short.objects.filter(sid=value)
        ud=subdetail.objects.filter(email=request.session['usr'])
        if ud[0].sub=="0":
            bol=False
            print("NO")
        else:
            bol=True
            print("YES")

        factory = qrcode.image.svg.SvgImage
        qr_string = f"upi://pay?pa={a[0].upiid}&pn=payment&am=0&cu=INR&"
        img = qrcode.make(qr_string, image_factory=factory, box_size=10)
        stream = BytesIO()
        img.save(stream)

        context = {
        'qrcode': stream.getvalue().decode(),'data':a[0],'bol':bol
        }





        # qrc=qrcode.make(f'upi://pay?pa={a[0].upiid}&pn=payment&am=0&cu=INR&')
        return render(request,'watchmedia.html',context)
    else:
        return redirect('fs:login')

def watchalbum(request,value=None):
    if request.session['usr']:
        context={}
        factory = qrcode.image.svg.SvgImage
        a=album.objects.filter(aid=value)
        ud=subdetail.objects.filter(email=request.session['usr'])
        if ud[0].sub=="0":
            bol=False
        else:
            bol=True
        factory = qrcode.image.svg.SvgImage
        qr_string = f"upi://pay?pa={a[0].upiid}&pn=payment&am=0&cu=INR&"
        img = qrcode.make(qr_string, image_factory=factory, box_size=10)
        stream = BytesIO()
        img.save(stream)

        context = {
        'qrcode': stream.getvalue().decode(),'data':a[0],'bol':bol
        }





        # qrc=qrcode.make(f'upi://pay?pa={a[0].upiid}&pn=payment&am=0&cu=INR&')
        return render(request,'watchmedia.html',context)
    else:
        return redirect('fs:login')
