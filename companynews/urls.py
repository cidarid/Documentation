from django.urls import path
from .views import article_list_view, article_detail_view, article_search_view

app_name = 'article'
urlpatterns = [
    path('', article_list_view, name="article-list"),
    path('<int:my_id>/', article_detail_view, name="article-detail"),
    path('search/', article_search_view, name="search_results"),
]
