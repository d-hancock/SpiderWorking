import scrapy
from tutorial.items import QuoteItem, QuoteLoader


class QuotesSpider1(scrapy.Spider):
    name = "quotes1"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            load = QuoteLoader(item=QuoteItem(), selector=quote, response=response)
            load.add_css(field_name='text', css='span.text::text')
            load.add_css(field_name='author', css='small.author::text')
            load.add_css(field_name='tags', css='div.tags a.tag::text')
            yield load.load_item()


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
