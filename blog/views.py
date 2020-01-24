from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404

from .models import Post


def search(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = post_list.filter(
            Q(Title__icontains=query)|
            Q(Content__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)



def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset


# Create your views here.
def blog_list(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:4]
    post_list = Post.objects.all()

    context = {
        'post_list':post_list,
        'most_recent':most_recent,
        'category_count':category_count
    }
    return render(request, 'blog.html',context )


def post(request, slug):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:4]
    posts = get_object_or_404(Post, slug = slug)

    context = {
        'posts':posts,
        'most_recent':most_recent,
        'category_count':category_count
    }
    return render(request, 'blog_details.html',context )
