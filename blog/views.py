from django.utils import timezone
from django.shortcuts import render
from .models import  Post
# Create your views here.


def list_view(request):
    posts = Post.objects.filter(status=Post.StatusChoices.PUBLISHED, publish_time__lte=timezone.now())
    return render(request, 'blog/list.html', {"posts": posts})


def detail_view(request, year, month, day, slug):
    return render(request, 'blog/detail.html', {"year": year, "month": month, "day": day, "slug": slug})
