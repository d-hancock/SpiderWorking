import scrapy
import itertools
from tutorial.items import MsrpItem, MsrpItemLoader


class MsrpSpider(scrapy.Spider):
    name = "msrp"
    allowed_domains = ['www.jdpower.com']

    def start_requests(self):
        makes = ['Acura', 'Aston-Martin', 'BMW', 'Buick', 'Cadillac',
                 'Chevrolet', 'Chrysler', 'Dodge', 'FIAT', 'Ford', 'GMC', 'Honda',
                 'Hummer', 'Hyundai', 'INFINITI', 'Jaguar', 'Jeep', 'Kia',
                 'Land-Rover', 'Lexus', 'Lincoln', 'Lotus', 'Mazda', 'Mercedes-Benz', 'Mitsubishi', 'Nissan',
                 'Oldsmobile', 'Panoz', 'Plymouth', 'Pontiac', 'Porsche',
                 'Ram-Truck', 'Scion', 'Subaru',
                 'Tesla-Motors', 'Toyota',
                 'Volkswagen', 'Volvo']

        def makes_urls(value):
            urls_list = []
            urls_list.append([f"https://www.jdpower.com/Cars/2019/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2018/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2017/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2016/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2015/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2014/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2013/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2012/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2011/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2010/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2009/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2008/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2007/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2006/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2005/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2004/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2003/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2002/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2001/{make}" for make in value])
            urls_list.append([f"https://www.jdpower.com/Cars/2000/{make}" for make in value])

            urls_list = list(itertools.chain.from_iterable(urls_list))
            # urls = [y for x in urls for y in x]

            return urls_list

        urls = makes_urls(makes)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for vehicle_bit in response.xpath('//div[contains(@class,"veh-spacer")]'):
            load = MsrpItemLoader(item=MsrpItem(), selector=vehicle_bit)
            load.add_xpath('full_name', '//*[contains(@class,"veh-icons__title")]/text()')
            load.add_xpath('full_name', './div/div/a/div/text()')
            load.add_xpath('year', '//*[contains(@class,"veh-icons__title")]/text()')
            load.add_xpath('make', '//*[contains(@class,"veh-icons__title")]/text()')
            load.add_xpath('vehicle_model', './div/div/a/div/text()')
            load.add_xpath('msrp_high',
                           './div/div[1]/div/span[contains(@class,"veh-group__attribute-value")]/text()')
            load.add_xpath('msrp_low',
                           './div/div[1]/div/span[contains(@class,"veh-group__attribute-value")]/text()')
            yield load.load_item()
