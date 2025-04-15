from django.shortcuts import render
from . import businesslogic
from django.http import HttpResponse

# Create your views here.
def test_page(request):
    return render(request,'comic/test.html',{
        
    })

def index(request):
    # Get the latest comic
    comic = businesslogic.GetCurrentComic()
    month = comic['month']
    year = comic['year']
    comicNumber = comic['num']
    Title = comic['safe_title']
    altText = comic['alt']
    image = comic['img']
    return render(request, 'comic/index.html',{
        'month': month,
        'year': year,
        'comicNumber': comicNumber,
        'Title': Title,
        'altText': altText, 
        'image': image
        
    })
       

#Get Next Comic 
def next(request):
    comic = businesslogic.GetNextComic()
    month = comic['month']
    year = comic['year']
    comicNumber = comic['num']
    Title = comic['safe_title']
    altText = comic['alt']
    image = comic['img']
    return render(request, 'comic/next.html',{
        'month': month,
        'year': year,
        'comicNumber': comicNumber,
        'Title': Title,
        'altText': altText, 
        'image': image
           
    }) 
    
#Get the previous comic
def previous(request):
     comic = businesslogic.GetPreviousComic()       
     month = comic['month']
     year = comic['year']
     comicNumber = comic['num']
     Title = comic['safe_title']
     altText = comic['alt']
     image = comic['img']
     return render(request, 'comic/previous.html',{
        'month': month,
        'year': year,
        'comicNumber': comicNumber,
        'Title': Title,
        'altText': altText, 
        'image': image 
    })
    
    
    
