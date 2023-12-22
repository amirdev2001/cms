from django.http import Http404
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# Create your views here.


def list_view(request):
    posts = Post.objects.filter(status=Post.StatusChoices.PUBLISHED, publish_time__lte=timezone.now())
    return render(request, 'blog/list.html', {"posts": posts})


def detail_view(request, year, month, day, slug):
    post = get_object_or_404(Post, status=Post.StatusChoices.PUBLISHED, publish_time__year=year, publish_time__month=month, publish_time__day=day, slug=slug)
    return render(request, 'blog/detail.html', {"post": post})

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {"categories": categories})