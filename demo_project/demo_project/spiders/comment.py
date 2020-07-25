import scrapy

class CommentSpider(scrapy.Spider):
    name = "po"

    start_urls = [ 'https://www.daraz.com.bd/#' ]

    def parse(self,response):
        page = response.url.split('/')[-1]

        html_file = 'po-%s.html' % page
        with open(html_file, 'wb') as f:
            f.write(response.body)