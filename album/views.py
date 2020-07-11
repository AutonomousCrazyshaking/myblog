from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import AlbumInfo


def album(request, id, page):
    albumList = AlbumInfo.objects.filter(user_id=id).order_by('id')
    paginator = Paginator(albumList, 8)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger:
        pageInfo = paginator.page(1)
    except EmptyPage:
        pageInfo = paginator.page(paginator.num_pages)
    return render(request, 'album.html', locals())
