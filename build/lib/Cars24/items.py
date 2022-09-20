# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Cars24Item(scrapy.Item):
    # define the fields for your item here like:
    car_title = scrapy.Field()
    variant = scrapy.Field()
    gear_box = scrapy.Field()
    mileage = scrapy.Field()
    owner = scrapy.Field()
    fuel_type = scrapy.Field()
    emi = scrapy.Field()
    price = scrapy.Field()
    record_create_date = scrapy.Field()
    site = scrapy.Field()
    source_country = scrapy.Field()
    feed_code = scrapy.Field()
    context_identifier = scrapy.Field()
    record_create_by = scrapy.Field()
    execution_id = scrapy.Field()
    pass
