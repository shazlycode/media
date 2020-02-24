from django.shortcuts import render, get_object_or_404
from app.models import TV
# Create your views here.
def index(request):
    tvsdrama=TV.objects.filter(tv_cat="drama")
    tvssport=TV.objects.filter(tv_cat="sport")
    tvsnews=TV.objects.filter(tv_cat="news")
    context={
        "title":"HOME",
        'tvsdrama':tvsdrama,
        'tvssport':tvssport,
        'tvsnews':tvsnews,
    }
    return render(request, 'app/index.html', context)

def player(request, channel_id):
    item=get_object_or_404(TV,id=channel_id)
    context={
        'title':'Channel Player',
        'media': item,
    }
    return render(request, 'app/mediaplayer.html', context)