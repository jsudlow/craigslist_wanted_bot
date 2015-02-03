#This bot attempts to connect to the craigs list wanted section.
#Once thre it goes through the top level paragraphs. These contain the links to the actual post we want to extract
#Once we fish the url out, we make another scrapy.Request call with a url and custom callback as arguments
#In our call back, we are scraping the actual post page itself. We grab the title and post and save them in our item.
#We yield the request and the item to make them persist when we want to make json data.

import scrapy
from cl_wanted_bot.items import CLItem

class CLSpidy(scrapy.Spider):
    name = "clspidy"
    allowed_domains = ["carbondale.craigslist.org"]
    start_urls = [
        "http://carbondale.craigslist.org/search/waa",
           ]

    def parse(self, response):
        for sel in response.xpath('//p'):
            url = sel.xpath('span[@class="txt"]/span[@class="pl"]/a/@href').extract()
            yield scrapy.Request('http://carbondale.craigslist.org' + url[0], callback=self.parse_clpost)
             
            
    def parse_clpost(self, response):
        item = CLItem()
        item['title'] = response.xpath('//title').extract()
        item['post'] = response.xpath('//body/article/section/section[@class="userbody"]/section[@id="postingbody"]/text()').extract()
        yield item
                