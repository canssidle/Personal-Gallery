from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404

from .models import Image


def welcome(request):

    images=Image.objects.all()
   

    return render(request,'welcome.html',{"images":images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"images":searched_images})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})


# # Create your views here.
