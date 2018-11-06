import scrapy
import colorama
from tutorial.items import InventoryItem, InventoryItemLoader


class DdcInventorySpider(scrapy.Spider):
    name = 'ddc_spider'
    allowed_domains = ['www.tompeckford.com']
    start_urls = ['https://www.tompeckford.com/new-inventory/index.htm']

    def parse(self, response):
        for inventory_vehicle in response.xpath('//div[contains(@class,"bd")]/ul/li/div[contains(@class,"auto")]'):
            load = InventoryItemLoader(item=InventoryItem(), selector=inventory_vehicle)
            load.add_xpath('full_name', './@data-year')
            load.add_xpath('full_name', './@data-make')
            load.add_xpath('full_name', './@data-model')
            load.add_xpath('year', './@data-year')
            load.add_xpath('make', './@data-make')
            load.add_xpath('vehicle_model', './@data-model')
            load.add_xpath('trim', './@data-trim')
            load.add_xpath('trim', './@data-trim')
            load.add_xpath('color', './@data-exteriorcolor')
            load.add_xpath('vin', './@data-vin')
            load.add_xpath('new_old', './@data-type')
            load.add_xpath('price',
                           '//div/div[2]/ul/li/span[contains(@class,"final-price")]/span[contains(@class,"value")]/text()')
            yield load.load_item()

        next_page = response.xpath('//*[@id="compareForm"]/div/div[1]/div/div/div[2]/ul/li[3]/a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
