from django.shortcuts import get_object_or_404, render
from .models import Tutorial


# Create your views here.
def article_detail_view(request, my_id):
    obj = get_object_or_404(Tutorial, id=my_id)
    context = {
        'object': obj
    }
    return render(request, "tutorialArticle.html", context)


def article_list_view(request):
    queryset = Tutorial.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "tutorialAll.html", context)


def article_search_view(request):
    searchquery = request.GET.get('q')
    if searchquery:
      queryset = Tutorial.objects.filter(title__icontains=searchquery) | Tutorial.objects.filter(summary__icontains=searchquery)
    else:
        return render(request, "tutorialSearchBar.html")
    context = {
        "object_list": queryset,
        "search_query": searchquery
    }
    return render(request, "tutorialSearch.html", context)
