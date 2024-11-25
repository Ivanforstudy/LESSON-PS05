import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div._tNHiT')
        for divan in divans:
            yield {
                'name' : divan.css('div.Pk6w8 GO3aC span: :text').get(),
                'price': divan.css('div.q5Uds T7z9Z span::text').get(),
                'url': divan.css('a').attrib['href']

            }
