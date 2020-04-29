from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from findusapp.form import *
from findusapp.models import *
# Create your views here.

def index(request):
    data=Cate.objects.all()
    data1=Subcate.objects.all()
    return render(request,'index.html',{'data':data,'data1':data1})

#-----------------------------------------------------
def addcate(request):
    if request.session.has_key('is_logged'):
        data=Cate.objects.all()
        if request.method=="POST" or request.method=="FILES":
            form=CateForm(request.POST,request.FILES)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('index')
                except:
                    print("error")
        else:
            form=CateForm()
        return render(request,'addcate.html',{'data':data})
    return redirect('login')
#---------------------------------------------------
def Edit_Delete_cate(request,sid,option):
    if request.session.has_key('is_logged'):
        data=Cate.objects.filter(id=sid).first()
        if option=='Delete':
            data.delete()
            return redirect('addcate')
        if option =='Edit':
            #if request.method=="POST" or request.method=="FILES":
            form=CateForm(request.POST,request.FILES, instance=data)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('addcate')
                except:
                    print("error")
        else:
            form=CateForm()
            return redirect('addcate')
        return render(request,'addcate.html',{'data':data})
    return redirect('login')
#-----------------------------------------------------------
def Edit_Delete_subcate(request,sid,option):
    if request.session.has_key('is_logged'):
        data1=Subcate.objects.filter(id=sid).first()
        if option=='Delete':
            data1.delete()
            return redirect('subcatepage')
        if option =='Edit':
            if request.method=="POST" or request.method=="FILES":
                data1.cate=request.POST['cate']
                data1.nameofsubcate=request.POST['nameofsubcate']
                data1.save()
                return redirect('subcatepage')
        return render(request,'subcatepage.html',{'data1':data1})
    return redirect('login')

def Login(request):
    error=False
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(username=username,password=password)
        if user:
            login(request,user)
            request.session['is_logged']=True
            return redirect('index')
        else:
            error=True
    return render(request,'loginform.html',{"error":error})

#-----------------------------------------------------------
def Logout(request):
    request.session['is_logged']=False
    logout(request)
    return redirect('index')

#------------------------------------------------------------
def registationpage(request):
    '''
    if not request.user.is_authenticated:
        return redirect('login')
        '''
    user=User.objects.all()
    data=user
    user_taken = False
    email_taken = False
    password_match = False
    if request.method=='POST':
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
                user_taken=True
                return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})
            elif User.objects.filter(email=email).exists():
                email_taken=True
                return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=fname,last_name=lname,)
                user.save()
                print('user created')
                return redirect('login')
        else:
            password_match=True
            return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})

        return redirect('reg')
    return render(request,'reg.html',{"data":data,'user_taken': user_taken,'email_taken': email_taken,'password_match':password_match})

#----------------------------------------------------------
def subcatepage(request):
    if request.session.has_key('is_logged'):
        data=Cate.objects.all()
        data1=Subcate.objects.all()
        if request.method=='POST':
            cate_id=request.POST['cate_id']
            nameofsubcate=request.POST['nameofsubcate']
            cat = Cate.objects.all().filter(id=cate_id).first()
            Subcate.objects.create(cate=cat,nameofsubcate=nameofsubcate)
            return redirect('index')
        return render(request,'subcatepage.html',{'data':data,'data1':data1})
    return redirect('login')
#----------------------------------------------------------------
def service(request):
    if request.session.has_key('is_logged'):
        return render(request,'service.html',{})
    return redirect('login')

#-----------------------------------------------------------------
def userview(request):
    if request.session.has_key('is_logged'):
        data=User.objects.all()
        return render(request,'userview.html',{'data':data})
    return redirect('login')

#------------------------------------------------------------------
def passwordmail(request):
	#data=student_detail.objects.all()
    if request.method=="POST":
        email=request.POST['email']
        try:
            subject = 'No Reply'
            message ='Your Password Reset Link are given Below ' 
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [str(email)]
            send_mail( subject, message, email_from, recipient_list )
            print('send')
        except Exception as e:
            print(e)
        return redirect('passwordmail')
    #return HttpResponse(render(request,"sms.html",{}))
    return render(request,'passwordmail.html',{})

























































