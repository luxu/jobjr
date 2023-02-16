import httpx
import parsel

LINE = '-' * 80

# url = "   https://www.adzuna.com.br/search?q=desenvolvedor&loc=107169"
# for tit, link in zip(texto.css('div.w-full div h2'), texto.css('div.w-full h2 a')):
#   titulo = ''.join(tit.css('a::text').getall()).strip()
#   url = link.xpath('@href').get()
#   print(f'{LINE}\n{titulo} - {url}')


BASE_URL = 'https://programathor.com.br/jobs'

response = httpx.get(BASE_URL)
texto = parsel.Selector(response.text)

caixas = texto.css('.cell-list')
for index, caixa in enumerate(caixas):
    if url := caixa.css('a').xpath('@href').get():
        titulo = caixa.css('.cell-list-content').css('h3::text').get()
        url = ''.join((BASE_URL, url))
        print(index, url)
        print(titulo)
