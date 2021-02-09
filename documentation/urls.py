from django.urls import path

from . import views

app_name = 'documentation'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_documentation/', views.new, name='new'),
    path('upload/', views.upload, name='upload'),
    path('new_category/', views.new_category, name='new_category'),
    path('<slug:cat_slug>-<int:cat_pk>/', views.category_view, name='category'),
    path('<slug:cat_slug>-<int:cat_pk>/edit', views.edit_category, name='edit_category'),
    path('<slug:cat_slug>-<int:cat_pk>/<slug:doc_slug>-<int:doc_pk>/', views.detail, name='detail'),
    path('<slug:cat_slug>-<int:cat_pk>/<slug:doc_slug>-<int:doc_pk>/edit/', views.edit, name='edit'),

]