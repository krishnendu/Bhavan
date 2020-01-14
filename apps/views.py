from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import user,FeedbackClass
from .forms import UserForm

# Create your views here.
def home(req):
    return render(req ,'base.html',navbar(req))

def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user1 = authenticate(username=username, password=raw_password)
            obj=user(id=User.objects.get(username=username).id)
            obj.save()
            print('The id is :', obj.id )
            
            login(req, user1)
            return redirect('home')
    else:
        form = UserCreationForm()
    ob1={'form' : form}
    ob1.update(navbar(req))
    return render(req, 'registration.html', ob1)

def login_view(req):
    if(req.method=='POST'):
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('/'+username)
        user = authenticate(req, email=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('/'+user.username)
        else:
            messages.error(req,"Username or Password does not match")
            return render(req,'login.html',navbar(req))

    else:
        return render(req,'login.html',navbar(req))
    


def logout_view(req):
    logout(req)
    return redirect('/')

def navbar(req):
    
    log='Log in'
    url='login'
    username='login'
    name='Krishnendu Chatterjee'
    phone_number='+917003033085'
    email='krishnenduchatterjee25@gmail.com'
    if req.user.is_authenticated:
        log='Log out'
        url='logout'
        username=req.user.username
    nav={ 'profile' : { 'name' : 'Profile' , 'url' : username},
    'log' : { 'name' : log , 'url' : url},
    'register' : {'name' : 'Register' , 'url' : 'register'},
    'copyright' : { 'name' : name , 'phone_number' : phone_number , 'email' : email ,}
    }
    return nav

def profile(req,username):
    if not req.user.is_authenticated:
        print('NOT Authenticated')
        return redirect('%s?next=%s' % (settings.LOGIN_URL, req.path))
    print('Authenticated')
    try:
        ob1={'user' : user.objects.get(id=User.objects.get(username=username).id)}
        ob1.update(navbar(req))
        ob2={ 'feedback' : {'name' : 'Feedback Form', 'url' : '/'+username+'/feedback'} }
        ob1.update(ob2)
        print(ob1)
        return render(req,'userinfo.html',ob1)
    except:
        return redirect('/'+username+'/edit')

def editprofile(req,username):
    if not req.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, req.path))
    id=user.objects.get(id=User.objects.get(username=username).id).id
    instance =get_object_or_404(user, id=id)
    #if(req.method == 'POST'):
    form=UserForm(req.POST or None, req.FILES or None ,instance=instance)
    if form.is_valid():
        form.save()
        email=form.cleaned_data.get('email')
        obj=User.objects.get(id=id)
        obj.email=email
        obj.save
        return redirect('/'+username)
    #else:
    #    form = UserForm()
    ob1={'form' : form}
    ob1.update(navbar(req))
    return render(req,'edit.html',ob1)
    #return HttpResponse('<h1>You can edit here</h1>')

def feedback_view(req,username):
    if not req.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, req.path))
    email=user.objects.get(id=User.objects.get(username=username).id).email
    if(req.method=='POST'):
        feedback=req.POST['feedback']
        obj=FeedbackClass(email=email,feedback=feedback)
        obj.save()
        return redirect('/'+username)
    else:
        return render(req,'feedback.html',navbar(req))
