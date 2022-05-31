from django.shortcuts import render
from .models import Article


def ret_all(request):
    return render(request, "blogApp/index.html", {"articles": Article.objects.all()})


def ret_sing(request, slug):
    return render(
        request, "blogApp/detail.html", {"article": Article.objects.get(slug=slug)}
    )
