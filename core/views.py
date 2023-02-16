from django.shortcuts import render
import httpx
import parsel


def index(request):
    template_name = 'core/index.html'
    context = {}
    return render(request, template_name, context)

def crawler(request):
    template_name = 'core/crawler.html'
    if request.method == 'GET':
        return render(request, template_name)
    else:
        # url = "https://www.adzuna.com.br/search?q=desenvolvedor&loc=107169"
        BASE_URL = 'https://programathor.com.br/jobs'

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
                url = ''.join((BASE_URL, url))
                item = {
                    'titulo': titulo,
                    'url': url
                }
                vagas_raspadas.append(item)
        context = {
            'url_vagas': BASE_URL,
            'vagas': vagas_raspadas
        }
        return render(request, template_name, context)
