from django.shortcuts import render
from app.models import TV
# Create your views here.
def index(request):
    tvs=TV.objects.all()
    context={
        "title":"HOME",
        'tvs':tvs,
    }
    return render(request, 'app/index.html', context)
