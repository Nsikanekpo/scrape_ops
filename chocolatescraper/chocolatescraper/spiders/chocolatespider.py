import scrapy
from chocolatescraper.itemsloaders import ChocolateProductLoader
from chocolatescraper.items import ChocolateProduct
from urllib.parse import urlencode
from environs import Env


# ✅ Load environment variables instead of hardcoding API key
env = Env()
env.read_env()
API_KEY = env.str("SCRAPEOPS_API_KEY")  # ✅ API key moved to .env


def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class ChocolateSpider(scrapy.Spider):

    # the name of the spider
    name = 'chocolatespider'

    # These are the urls that we will start scraping
    def start_requests(self):
        start_url = 'https://www.chocolate.co.uk/collections/all'
        yield scrapy.Request(url=get_proxy_url(start_url), callback=self.parse)

    
    def parse(self, response):
        products = response.css('product-item')

        for product in products:
            chocolate = ChocolateProductLoader(item=ChocolateProduct(), selector=product)
            chocolate.add_css('name', "a.product-item-meta__title::text")
            chocolate.add_css('price', 'span.price', re='<span class="price">\n              <span class="visually-hidden">Sale price</span>(.*)</span>')
            chocolate.add_css('url', 'div.product-item-meta a::attr(href)')
            yield chocolate.load_item()

        next_page = response.css('[rel="next"] ::attr(href)').get()

        if next_page is not None:
           next_page_url = 'https://www.chocolate.co.uk' + next_page
           yield scrapy.Request(url=get_proxy_url(next_page_url), callback=self.parse)

        
        

       