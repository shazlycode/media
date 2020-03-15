from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app.models import TV, Radio
from app.forms import RegisterForm, LogForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    
    tvsdrama=TV.objects.filter(tv_cat="drama")
    tvssport=TV.objects.filter(tv_cat="sport")
    tvsnews=TV.objects.filter(tv_cat="news")
    tvsrel=TV.objects.filter(tv_cat="rel")
    context={
        "title":"HOME",
        'tvsdrama':tvsdrama,
        'tvssport':tvssport,
        'tvsnews':tvsnews,
        'tvsrel':tvsrel,
    }
    return render(request, 'app/index.html', context)

def ChannelPlayer(request, channel_id):
    is_favorite=False
    item=get_object_or_404(TV,id=channel_id)
    if item.favorite.filter(id=request.user.id).exists():
        is_favorite= True

    context={
        'title':'Channel Player',
        'media': item,
        'is_favorite': is_favorite,
    }
    return render(request, 'app/channelplayer.html', context)


def radio(request):
    radiosquran=Radio.objects.filter(radio_cat='quran')
    context={
        'title':'Radio',
        'radiosquran':radiosquran,

    }
    return render(request, 'app/radio.html', context)


def RadioPlayer(request, radio_id):
    item=get_object_or_404(Radio,id=radio_id)
    context={
        'title':'Radio Player',
        'radioitem': item,
    }
    return render(request, 'app/radioplayer.html', context)

def register(request):
    registerform= RegisterForm()
    if request.method=="POST":
        registerform=RegisterForm(request.POST)
        if registerform.is_valid():
            newform=registerform.save(commit='False')
            username=registerform.cleaned_data['username']
            password=registerform.cleaned_data['password1']
            newform.set_password(password)
            newform.save()
            messages.success(request,'congratulations {} You have successfully registered'.format(username))
            return redirect('login')


    else:
        registerform=RegisterForm()
    context={
        'title':'Register',
        'registerform':registerform,

    }
    return render(request, 'app/register.html', context)

def log(request):
    if request.method=='POST':
        logform=LogForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have successfully logedin {}'.format(username))
            return redirect('index')
        else:
            messages.warning(request,'You are not registered')
            return redirect('login')

    else:
        logform=LogForm()
    context={
        'title':'Login',
        'logform':logform,

    }
    return render(request, 'app/login.html', context)

def logout_user(request):
    logout(request)
    context={
        'title':'Logout',
    }
    return render(request, 'app/logout.html', context)


def favorite_channel(request, id):
    tv=get_object_or_404(Tv, id=id)
    if tv.favorit.filter(id=request.user.id).exists():
        tv.favorit.remove(request.user)
    else:
        tv.favorit.add(request.user)
    return HTTPRespondRedirect(tv.get_absolute_url())