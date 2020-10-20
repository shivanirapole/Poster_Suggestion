# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
'''
    THIS FILE IS FOR ITEM CONTAINER TEMPLATE
    Scraped Data > Item Containers > Json/csv files 
'''

class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # ITEM CONTAINER
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    pass

class ImageItem(scrapy.Item):
    name = scrapy.Field()
    img_url = scrapy.Field()
