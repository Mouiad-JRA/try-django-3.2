from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from articles.models import Article


# def article_detail_view(request, *args, **kwargs):
def article_detail_view(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = {
        "article": article
    }
    return render(request, "article-detail.html", context=ctx)
