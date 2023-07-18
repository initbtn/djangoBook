from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark
from django.template.context_processors import request

# Create your views here.
def detail(request):
    addr=request.GET['url']
    # select * from bookmark where url=addr
    dto=Bookmark.objects.get(url=addr)
    return render(request, 'bookmark/detail.html',{'dto':dto})


def list(request):
    # select * from bookmark order by title
    urlList=Bookmark.objects.all().order_by('-title')
    # select count(*) from bookmark
    urlCount=Bookmark.objects.all().count()
    
    return render(request, 'bookmark/list.html',{'urlList':urlList,'urlCount':urlCount})    

class BookmarkLV(ListView):
    model=Bookmark

class BookmarkDV(DetailView):
    model=Bookmark