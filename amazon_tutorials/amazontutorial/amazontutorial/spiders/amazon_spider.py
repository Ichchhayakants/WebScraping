# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.in/gp/bestsellers/books/1318068031/ref=zg_bs_nav_b_1_b']

    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css('.p13n-sc-truncated::text').extract()
        product_author = response.css('.a-link-child').css('::text').extract()
        product_price = response.css('.p13n-sc-price').css('::text').extract()
        #product_imagelink = response.css('img::attr(src').extract()


        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        #items['product_imagelink'] = product_imagelink

        yield items

