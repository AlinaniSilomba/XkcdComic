from django.shortcuts import render
from . import businesslogic

# Create your views here.
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