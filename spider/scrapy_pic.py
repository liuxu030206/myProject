import scrapy

class ChinazSpider(scrapy.Spider):
    name = 'chinaz'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['https://sc.chinaz.com/tupian/index.html']

    def parse(self, response):
        img_urls = response.xpath('//div[@class="tupian-list com-img-txt-list masonry"]/div/div/a/img/@src')
        for img_url in img_urls:
            yield {'image_urls': [img_url.get()]}
