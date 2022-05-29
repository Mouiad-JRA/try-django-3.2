from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from articles.forms import ArticleForm
from articles.models import Article


# def article_detail_view(request, *args, **kwargs):
@login_required
def article_detail_view(request, pk):
    # article = Article.objects.get(pk=kwargs.get('pk'))
    article = Article.objects.get(pk=pk)
    ctx = {
        "article": article
    }
    return render(request, "articles/article-detail.html", context=ctx)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    ctx = {
        "form": form
    }
    if form.is_valid():
        obj = form.save()
        ctx['form'] = ArticleForm()
        ctx['created'] = True
        ctx['object'] = obj

    return render(request, "articles/create.html", context=ctx)


@login_required
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
