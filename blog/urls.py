from django.urls import path
from . import views



app_name = 'blog'
urlpatterns = [
    path('', views.blog_list, name='blog-posts'),
    path('<slug>/', views.post, name='blog-details'),
    path('Search-Results/', views.search, name='s-results'),
]
