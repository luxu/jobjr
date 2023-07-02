import httpx
import parsel

LINE = '-' * 80

BASE_URL = 'https://programathor.com.br/jobs'

response = httpx.get(BASE_URL)
texto = parsel.Selector(response.text)

caixas = texto.css('.cell-list')
for index, caixa in enumerate(caixas):
    if url := caixa.css('a').xpath('@href').get():
        titulo = caixa.css('.cell-list-content').css('h3::text').get()
        empresa = caixa.css('.cell-list-content').css('span::text')[0].getall()[0]
        if 'NOVA' in empresa:
            empresa = caixa.css('.cell-list-content').css('span::text')[1].getall()[0]
        url = ''.join((BASE_URL, url))
        print(index, url)
        print(empresa)
        print(titulo)
