from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404

from main.forms import URLShortenerForm
from main.misc import get_random_token
from main.models import Link


def index(request):
    if request.method == 'POST':
        form = URLShortenerForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            token = get_random_token()
            Link.objects.create(
                url=url,
                token=token,
            )
            return redirect('preview', token=token)

    else:
        form = URLShortenerForm()

    return render(request, 'main/index.html', {'form': form})


def preview(request, token):
    link = get_object_or_404(Link, token=token)
    short_url = '{}/{}'.format(settings.DOMAIN, link.token)

    return render(request, 'main/preview.html', {
        'url': link.url,
        'short_url': short_url,
    })


def redirect_to(request, token):
    link = get_object_or_404(Link, token=token)
    link.clicks_count += 1
    link.save()
    return HttpResponseRedirect(link.url)


def stats(request):
    links = Link.objects.all()
    paginator = Paginator(links, 10)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/stats.html', {
        'page_obj': page_obj,
    })
