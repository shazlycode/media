from django.shortcuts import render, get_object_or_404
from app.models import TV, Radio
from app.forms import RegisterForm
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
    item=get_object_or_404(TV,id=channel_id)
    context={
        'title':'Channel Player',
        'media': item,
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
    context={
        'title':'Register',
        'registerform':registerform,

    }
    return render(request, 'app/register.html', context)