# -*- coding: utf-8 -*-  

from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector  
from loupan.items import LoupanItem  


class Loupan(CrawlSpider):  
    name = "loupan"  
    start_urls = ['https://sh.focus.cn/loupan/']  

    url = 'https://sh.focus.cn/loupan/'
    def parse(self,response):  
        #print response.body  
        item = LoupanItem()  
        selector = Selector(response)  
        #print selector  
        Houses = selector.xpath('//div[@class="list"]')  
        #print house  
        for eachHouse in Houses:  
            title = eachHouse.xpath('div[@class="txt-center"]/div[@class="title"]/a/text()').extract()
            price = eachHouse.xpath('div[@class="txt-right"]/p[1]/text()').extract()
            danwei = eachHouse.xpath('div[@class="txt-right"]/p/span[1]/text()').extract()
            #print title and item
            item['title'] = title  
            item['price'] = price
            item['danwei']= danwei
            yield item
            #循环
            '''def start_requests(self):
                for x in range(1, 680):
                    yield scrapy.Request("https://house.focus.cn/loupan/p{0}".format(x), callback=self.parse)'''
            
            nextLink = selector.xpath('//*[@id="bd-left"]/div[3]/a[10]/@href').extract()
            # 第10页是最后一页，没有下一页的链接  
            if nextLink:  
                nextLink = nextLink[0]  
                print nextLink  
                yield Request(nextLink, callback=self.parse)

                '''item1 = Item()
                   yield item1
                   item2 = Item()
                   yield item2
                   req = Request(url='下一页的链接', callback=self.parse)
                   yield req'''

