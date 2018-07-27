import scrapy

class KanjiSpider(scrapy.Spider):
    name = "kanji_spider"
    endpoint = "https://jisho.org/search/"
    text_file = open("kanji.txt")
    start_urls = []
    urls = text_file.readlines()
    for value in urls:
        start_urls.append(endpoint+value.rstrip())

    def parse(self, response):
        print response.url
        print "\n"
        DICT_SELECTOR = ".no-bullet li"
        for item in response.css(DICT_SELECTOR):
            print item.css("a ::attr(href)").extract_first()
            
