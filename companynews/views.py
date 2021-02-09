from django.shortcuts import get_object_or_404, render
from .models import Article


# Create your views here.
def article_detail_view(request, my_id):
    obj = get_object_or_404(Article, id=my_id)
    context = {
        'object': obj
    }
    return render(request, "newsArticle.html", context)


def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "newsAll.html", context)


def article_search_view(request):
    searchquery = request.GET.get('q')
    if searchquery:
      queryset = Article.objects.filter(title__icontains=searchquery) | Article.objects.filter(summary__icontains=searchquery)
    else:
        return render(request, "newsSearchBar.html")
    context = {
        "object_list": queryset,
        "search_query": searchquery
    }
    return render(request, "newsSearch.html", context)
