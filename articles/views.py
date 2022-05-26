from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from articles.models import Article


# def article_detail_view(request, *args, **kwargs):
def article_detail_view(request, pk):
    # article = Article.objects.get(pk=kwargs.get('pk'))
    article = Article.objects.get(pk=pk)
    ctx = {
        "article": article
    }
    return render(request, "articles/article-detail.html", context=ctx)


def article_create_view(request):
    ctx = {}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.create(title=title, content=content)
        ctx['title'] = title
        ctx['content'] = content
        ctx['created'] = True
        ctx['object'] = article

    return render(request, "articles/create.html", context=ctx)


def article_search_view(request):
    try:
        query = int(request.GET.get("query"))
    except:
        query = None
    article = None
    if query:
        article = Article.objects.get(pk=query)
    ctx = {
        'object': article
    }
    return render(request, "articles/search.html", context=ctx)
