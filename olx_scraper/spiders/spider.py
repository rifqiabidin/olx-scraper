import scrapy


class OlxSpider(scrapy.Spider):
    name = "olx-spider"
    allowed_domains = ["olx.co.id"]
    start_urls = ['https://www.olx.co.id/bandung-kota_g4000018/disewakan-rumah-apartemen_c5160?filter=type_eq_rumah']

    def parse(self,response):
        self.log(response.url+' Visited')
        for ad in response.css('li.EIR5N'):
            item = {
                'link': ad.css('a::attr(href)').extract_first(),
                'harga': ad.css('span._89yzn::text').extract_first(),
                'room': ad.css('span._2TVI3::text').extract_first(),
                'lokasi': ad.css('span.tjgMj::text').extract_first(),
                'date': ad.css('span.zLvFQ > span::text').extract_first()
            }
            yield(item)

