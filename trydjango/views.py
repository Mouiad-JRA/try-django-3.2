from django.http import HttpResponse
from django.template.loader import render_to_string, get_template

from articles.models import Article


def home(request):
    obj = Article.objects.all().first()
    queryset = Article.objects.all()
    context = {
        "object_list": queryset,
    }
    temp = get_template("home-view.html")
    temp_string = temp.render(context=context)
    return HttpResponse(temp_string)
