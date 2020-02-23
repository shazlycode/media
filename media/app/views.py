from django.shortcuts import render
from app.models import TV
# Create your views here.
def index(request):
    tvsdrama=TV.objects.filter(tv_cat="drama")
    tvssport=TV.objects.filter(tv_cat="sport")
    context={
        "title":"HOME",
        'tvsdrama':tvsdrama,
        'tvssport':tvssport,
    }
    return render(request, 'app/index.html', context)
