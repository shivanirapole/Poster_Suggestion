# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
'''
    Scraped Data > Item Containers > Json/csv files 
    Scraped Data > Item Containers > Pipeline > SQL/MongoDB database
    To activate pipelines.py uncomment the corresponding code in settings.py. Now every time yield is sent through pipeline function 
'''

class QuotetutorialPipeline:
    def process_item(self, item, spider):
        print('Pipeline : '+item['img_url'][0])
        return item
