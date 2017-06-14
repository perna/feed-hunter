# -*- coding: utf-8 -*-
import scrapy

class ItunesSpider(scrapy.Spider):
    name = 'itunes'
    start_urls = [
            'https://itunes.apple.com/us/genre/podcasts-arts/id1301?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-business/id1321?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-comedy/id1303?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-education/id1304?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-games-hobbies/id1323?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-government-organizations/id1325?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-health/id1307?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-kids-family/id1305?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-music/id1310?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-news-politics/id1311?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-religion-spirituality/id1314?mt=2/',
            'https://itunes.apple.com/us/genre/podcasts-science-medicine/id1315?mt=2',
            'https://itunes.apple.com/us/genre/podcasts-society-culture/id1324?mt=2',
            'https://itunes.apple.com/us/genre/podcasts-sports-recreation/id1316?mt=2',
            'https://itunes.apple.com/us/genre/podcasts-tv-film/id1309?mt=2',
            'https://itunes.apple.com/us/genre/podcasts-technology/id1318?mt=2',
        ]


    def parse(self, response):
        items = response.xpath('//*[@id="selectedgenre"]/ul/li')

        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_page) 

    
    def parse_page(self, response):
        items = response.xpath('//*[@id="selectedgenre"]/ul[2]/li')

        for item in items:
            page = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=page, callback=self.parse_list)


    def parse_list(self, response):
        for url in response.xpath('//*[@id="selectedcontent"]/div/ul/li'):
            podcast = url.xpath('./a')
            yield {
                    'name': podcast.xpath('./text()').extract_first(),
                    'url': podcast.xpath('./@href').extract_first()
                  }