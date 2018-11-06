import scrapy
from scrapy.loader import ItemLoader
from scrapy.item import Item
from scrapy.loader.processors import MapCompose, Join, TakeFirst


def filter_models(value):
    return value.replace(' models', '')


def make_processor(value):
    x = value.split()
    y = x[1]
    return y


def clean_text(value):
    return value.strip()


def year_processor(value):
    x = value.split()
    y = x[0]
    return y


def msrp_func_low(value):
    x = value.split(" ")
    y = x[0].replace('$', '')
    z = y.replace(',', '')
    if z == "N/A":
        return z
    else:
        a = float(z)
        return a


def msrp_func_high(value):
    x = value.split(" ")
    y = x[-1].replace('$', '')
    z = y.replace(',', '')
    if z == "N/A":
        return z
    else:
        a = float(z)
        return a


class MsrpItemLoader(ItemLoader):
    default_input_processor = MapCompose(clean_text)
    default_output_processor = TakeFirst()

    full_name_in = MapCompose(filter_models, clean_text)
    full_name_out = Join(separator=" ")

    msrp_high_in = MapCompose(msrp_func_high)

    msrp_low_in = MapCompose(msrp_func_low)

    make_in = MapCompose(make_processor)

    year_in = MapCompose(year_processor)

    price_in = MapCompose(msrp_func_low)


class MsrpItem(scrapy.Item):
    full_name = scrapy.Field()
    year = scrapy.Field()
    make = scrapy.Field()
    vehicle_model = scrapy.Field()
    msrp_high = scrapy.Field()
    msrp_low = scrapy.Field()


class QuoteItem(Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class QuoteLoader(ItemLoader):
    default_input_processor = MapCompose(clean_text)
    default_output_processor = TakeFirst()

    full_name_out = Join()

    price_in = MapCompose(msrp_func_low)


class InventoryItem(Item):
    full_name = scrapy.Field()
    year = scrapy.Field()
    make = scrapy.Field()
    vehicle_model = scrapy.Field()
    trim = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    vin = scrapy.Field()
    new_old = scrapy.Field()


class InventoryItemLoader(ItemLoader):
    default_input_processor = MapCompose(clean_text)
    default_output_processor = TakeFirst()

    full_name_out = Join()

    price_in = MapCompose(msrp_func_low)
