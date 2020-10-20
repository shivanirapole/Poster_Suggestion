import scrapy
from ..items import QuotetutorialItem
from ..items import ImageItem
import time
import random

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        # 'https://myanimelist.net/topanime.php'
        'https://quotes.toscrape.com/page/1/'
    ]
    # scrapy expects name, start_url variables and parse function

    def parse(self,response):

        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
            # yield {
            #     'title' : title,
            #     'author' : author,
            #     'tag' : tag
            # }

        # for pages which have next button
        #next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)


        next_page = 'https://quotes.toscrape.com/page/'+str(QuoteSpider.page_number)+'/'
        if QuoteSpider.page_number <= 10:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

class ImgSpider(scrapy.Spider):
    name = 'images'
    current_limit = 50
    img_urls = []
    start_urls = [
        'https://myanimelist.net/topanime.php?type=movie&limit=0'
        # 'https://myanimelist.net/anime/32281/Kimi_no_Na_wa'
    ]

    def parse(self, response):
        item = ImageItem()
        img_urls = []
        for site_url in response.css("h3.hoverinfo_trigger a::attr(href)").extract():
            yield scrapy.Request(site_url, callback=self.parse_site_url)

        next_page = 'https://myanimelist.net/topanime.php?type=movie&limit='+ str(ImgSpider.current_limit)

        if ImgSpider.current_limit <=3000:
            ImgSpider.current_limit +=50
            yield response.follow(next_page, callback=self.parse)


    def parse_site_url(self, response):
        # ImgSpider.img_urls.append(response.css('.borderClass div div .lazyload::attr(data-src)').get())
        sleep_time = random.randint(0, 10)
        time.sleep(sleep_time)
        print('slept for '+str(sleep_time)+' seconds :P')
        img_url = response.css('.borderClass div div .lazyload::attr(data-src)').extract()
        name = response.css('title::text').get()
        name = name.split('-')[0]
        name = name[1:]
        print("______________________________"+name)
        item = ImageItem()
        item['name'] = name
        item['img_url'] = img_url
        yield item














