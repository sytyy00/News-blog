from django.shortcuts import render
from .models import Articles
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.context_processors import csrf


def articles(request):
    articles_list = Articles.objects.all().order_by("-date")
    paginator = Paginator(articles_list,5)
    page = request.GET.get('page',1)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'news/posts.html', {'articles': articles})


def article(request, article_id=1):
    args = {}
    args.update(csrf(request))
    args['article'] = Articles.objects.get(id=article_id)
    return render(request, 'news/post.html', args)



