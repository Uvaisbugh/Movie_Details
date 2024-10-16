from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie
# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list':movie
    }
    return  render(request,'index.html',context)


def details(request,MID):
    MV= Movie.objects.get(id=MID)
    return render(request,"details.html",{'movie':MV})


def add(request):
    if request.method=='POST':
        name=request.POST.get('Name',)
        year=request.POST.get('Year',)
        Description=request.POST.get('Description',)
        img=request.FILES['img']
        movie=Movie(name=name,desc=Description,year=year,img=img)
        movie.save()
        return redirect('/')

    return render(request,'add.html')

def update(request,Id):
    movie = Movie.objects.get(id=Id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,Id):
    if request.method == 'POST':
        MV = Movie.objects.get(id=Id)
        MV.delete()
        return redirect('/')
    return render(request,'delete.html')