import scrapy

class GetURL(scrapy.Spider):
    name = "get_urls"
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
            with open("links.txt", "a") as myfile:
                myfile.write(item.css("a ::attr(href)").extract_first()+"\n")
