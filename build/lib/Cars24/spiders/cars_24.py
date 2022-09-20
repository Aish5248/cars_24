import scrapy
from datetime import date
from ..items import Cars24Item


class Cars24Spider(scrapy.Spider):
    name = 'cars_24'
    project_id = 'carID123'

    allowed_domains = ['www.cars24.com']
    start_urls = ['https://www.cars24.com/buy-used-car']

    def parse(self, response):
        items = Cars24Item()  # Object to store data in items.py
        cars = response.css('div._1l4fi')  # Selecting product container
        for car in cars:
            selector = scrapy.Selector(text=car.get())
            car_title = selector.css('h2._3FpCg::text').get()
            variant = selector.css('p.cvakB::text').get()
            gear_box = selector.css('.cvakB span::text').get()
            mileage = selector.css('.bVR0c li::text').get()
            owner = selector.css('.bVR0c li:nth-child(2)::text').get()
            fuel_type = selector.css('.bVR0c li~ li+ li::text').get()
            emi = selector.css('._2HFRN strong::text').get()
            price = selector.css('._7udZZ span::text').get()


            items['car_title'] = car_title
            items['variant'] = variant
            items['gear_box'] = gear_box
            items['mileage'] = mileage
            items['owner'] = owner
            items['fuel_type'] = fuel_type
            items['emi'] = emi
            items['price'] = price
            items['record_create_date'] = str(date.today())
            items['site'] = 'www.cars24.com'
            items['source_country'] = 'IND'
            items['feed_code'] = 'carID123'
            items['context_identifier'] = 'Used car in india'
            items['record_create_by'] = 'carID123_cars24_usedcar'
            items['execution_id'] = '621097'  # This will be taken automatically from zyte , as of now this is hardcoded

            yield items
