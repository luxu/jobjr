import json
from http import HTTPStatus

import httpx
import parsel
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import resolve_url

from core.models import Job

DEFAULT_PAGE_SIZE = 25


def index(request):
    template_name = 'core/index.html'
    jobs = Job.objects.all()
    context = {
        'jobs': jobs
    }
    return render(request, template_name, context)


def crawler(request):
    template_name = 'core/crawler.html'
    if request.method == 'GET':
        return render(request, template_name)
    else:
        # url = "https://www.adzuna.com.br/search?q=desenvolvedor&loc=107169"
        BASE_URL = 'https://programathor.com.br/jobs/'

        response = httpx.get(BASE_URL)
        texto = parsel.Selector(response.text)

        vagas_raspadas = []
        # for tit, link in zip(texto.css('div.w-full div h2'), texto.css('div.w-full h2 a')):
        caixas = texto.css('.cell-list')
        for caixa in caixas:
            # titulo = ''.join(tit.css('a::text').getall()).strip()
            # url = link.xpath('@href').get()
            if url := caixa.css('a').xpath('@href').get():
                titulo = caixa.css('.cell-list-content').css('h3::text').get()
                url = ''.join((BASE_URL, url.split('jobs')[1]))
                item = {
                    'titulo': titulo,
                    'url': url
                }
                vagas_raspadas.append(item)
        context = {
            'url_vagas': BASE_URL,
            'vagas': vagas_raspadas,
            'vagas_json': json.dumps(vagas_raspadas),
        }
        return render(request, template_name, context)


def salvar(request):
    template_name = 'core/salvar.html'
    data = request.GET['vagas']
    vagas = json.loads(data)
    # jobs = Job.objects.create(**vagas)
    for r in vagas:
        titulo = r['titulo']
        url = r['url']
        Job.objects.create(
            titulo=titulo,
            url=url
        )
    # response = JsonResponse(jobs.to_dict(), status=HTTPStatus.CREATED)
    # response['Location'] = resolve_url(jobs)
    # return response
    return render(request, template_name)

def salvar_api(request):

    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', DEFAULT_PAGE_SIZE)

    queryset = Job.objects.all()
    if q := request.GET.get('q'):
        queryset = queryset.filter(name__icontains=q)

    paginator = Paginator(queryset, per_page=page_size)
    page = paginator.get_page(page_number)

    return JsonResponse(page2dict(page))

def page2dict(page):
    return {
        'data': [a.to_dict() for a in page],
        'count': page.paginator.count,
        'current_page': page.number,
        'num_pages': page.paginator.num_pages
    }