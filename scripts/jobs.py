import httpx
import parsel

LINE = '-'*80

url = "https://www.adzuna.com.br/search?q=desenvolvedor&loc=107169"

response = httpx.get(url)
texto = parsel.Selector(response.text)

for tit, link in zip(texto.css('div.w-full div h2'), texto.css('div.w-full h2 a')):
  titulo = ''.join(tit.css('a::text').getall()).strip()
  url = link.xpath('@href').get()
  print(f'{LINE}\n{titulo} - {url}')
