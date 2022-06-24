import scrapy

class YqsjProvinceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    location = scrapy.Field()
    new = scrapy.Field()
    exist = scrapy.Field()
    total = scrapy.Field()
    cure = scrapy.Field()
    dead = scrapy.Field()
