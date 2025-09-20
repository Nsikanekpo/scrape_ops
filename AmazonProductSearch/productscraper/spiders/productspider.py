import scrapy

import os
from urllib.parse import urlencode
from dotenv import load_dotenv



load_dotenv()
API_KEY = os.getenv("SCRAPEOPS_API_KEY")

def get_proxy_url(url):
    payload = {"api_key": API_KEY, "url": url}
    proxy_url = "https://proxy.scrapeops.io/v1/?" + urlencode(payload)
    return proxy_url


class ProductspiderSpider(scrapy.Spider):
    name = "productspider"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=ipad&crid=1ZY02724OXD57&sprefix=ipad%2Caps%2C432&ref=nb_sb_noss_1"]

    def parse(self, response):
        pass
