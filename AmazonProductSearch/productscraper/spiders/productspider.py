import scrapy
from urllib.parse import urljoin
import re
import json


class ProductspiderSpider(scrapy.Spider):
    name = "productspider"
    allowed_domains = ["amazon.com", "proxy.scrapeops.io"]

    # Starting with one search term
    start_urls = [
        "https://www.amazon.com/s?k=ipad&crid=1ZY02724OXD57&sprefix=ipad%2Caps%2C432&ref=nb_sb_noss_1"
    ]

    def parse(self, response):
        products = response.css('div.s-main-slot div[data-component-type="s-search-result"]')
    
        for product in products:
            yield {
                'title': product.css('h2 a span::text').get(),
                'link': response.urljoin(product.css('h2 a::attr(href)').get()),
                'price': product.css('.a-price .a-offscreen::text').get(),
                'rating': product.css('.a-icon-alt::text').get(),
                'reviews': product.css('span.a-size-base.s-underline-text::text').get(),
            }

        # --- Handle Pagination ---
        next_page = response.css("a.s-pagination-next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
