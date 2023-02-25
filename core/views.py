import json
from http import HTTPStatus

import httpx
import parsel
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
    BASE_URL = 'https://programathor.com.br/jobs/'

    response = httpx.get(BASE_URL)
    texto = parsel.Selector(response.text)

    vagas_raspadas = []
    caixas = texto.css('.cell-list')
    for caixa in caixas:
        if url := caixa.css('a').xpath('@href').get():
            titulo = caixa.css('.cell-list-content').css('h3::text').get()
            url = ''.join((BASE_URL, url.split('jobs')[1]))
            item = {'titulo': titulo, 'url': url}
            vagas_raspadas.append(item)
    context = {
        'url_vagas': BASE_URL,
        'vagas': vagas_raspadas,
        'vagas_json': json.dumps(vagas_raspadas),
    }
    return render(request, template_name, context)

def crawler_api(request):
    BASE_URL = 'https://programathor.com.br/jobs/'
    response = httpx.get(BASE_URL)
    texto = parsel.Selector(response.text)
    caixas = texto.css('.cell-list')
    for caixa in caixas:
        if url := caixa.css('a').xpath('@href').get():
            titulo = caixa.css('.cell-list-content').css('h3::text').get()
            url = ''.join((BASE_URL, url.split('jobs')[1]))
            Job.objects.create(
                titulo=titulo,
                url=url
            )
    return JsonResponse('Dados salvos com sucesso!', status=HTTPStatus.CREATED, safe=False)

def salvar(request):
    template_name = 'core/salvar.html'
    data = request.GET['vagas']
    vagas = json.loads(data)
    for r in vagas:
        titulo = r['titulo']
        url = r['url']
        Job.objects.create(
            titulo=titulo,
            url=url
        )
    return render(request, template_name)


@csrf_exempt
def salvar_api(request):
    titulo = request.POST.get('titulo')
    url = request.POST.get('url')
    if titulo:
        data = {
            'titulo': titulo,
            'url': url
        }
        job = Job.objects.create(**data)
        return JsonResponse(job.to_dict(), status=HTTPStatus.CREATED)
    else:
        return JsonResponse('Não veio os dados. Reveja!', status=HTTPStatus.BAD_REQUEST)


def excluir(request):
    if vagas := Job.objects.all():
        vagas.delete()
        context = {'msg': "OK"}
    else:
        context = {'msg': "Não há vagas a serem apagadas!"}
    return JsonResponse(context)


def listar_api(request):
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', DEFAULT_PAGE_SIZE)

    queryset = Job.objects.all()

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
