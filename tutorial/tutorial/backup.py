import scrapy
from ..items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self,response):
        items = TutorialItem()
        # title = response.css('title::text').extract()
        # yield {'titletext':title}
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            items['title']=title
            items['author'] = author
            items['tag'] = tag
            yield items

        # next_page = response.css("li.next a::attr(href)").get()
        #
        # if next_page is not None:
        #     yield response.follow(next_page,callback=self.parse)

        next_page ='http://quotes.toscrape.com/page/2/'+ str(QuotesSpider.page_number)+'/'
        if QuotesSpider.page_number < 11:
            QuotesSpider.page_number +=1
            yield response.follow(next_page, callback=self.parse)
