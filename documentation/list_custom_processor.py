from .models import Category, Documentation


def category_renderer(request):
    return {
        'all_categories': Category.objects.all()
    }


def doc_renderer(request):
    return {
        'all_documentation': Documentation.objects.all()
    }