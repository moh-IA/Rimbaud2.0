from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from .models import Area
from .models import Article

# Create your views here.
def home (request):
    areas = Area.objects.all()
    articles = Article.objects.all()
    return render (request,'home.html',{ 'areas':areas,'articles':articles})

    # areas_name = []
    # for area in areas:
    #     areas_name.append(area.name)
    
    # return HttpResponse(areas_name)
def article (request, article_id):
    article = Article.objects.get(pk= article_id)
    area = Area.objects.get(pk = article.area_id)
    return render (request,"article.html", {'article':article, 'area': area})


# search articles by id 
def search_article (request):
    if request.method == "POST":
        search = request.POST.get('search')
        id_search = all(map(str.isdigit, search))
        to_day = datetime.date.today()
        
        print(to_day)
        
        if search != '' and id_search:
            articles= []  
            try:
                article = Article.objects.get(pk = search)
                articles.append(article)
                
            except Article.DoesNotExist:
                raise Http404("Article does not exist !! try with a valide article id")
            return render(request, 'search_articles.html', {'articles':articles, 'search':search,'to_day':to_day})
        # Bonus 1
        elif search != '' and not id_search: 
            try:
                articles = Article.objects.all().filter(title__contains= search)
            except Article.DoesNotExist:
                raise Http404("Article does not exist !!")
            return render(request, 'search_articles.html', {'articles':articles, 'search':search,'to_day':to_day})

        else:
            return render(request, 'search_articles.html', {'search':search})
      

