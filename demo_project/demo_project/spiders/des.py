import scrapy
# from srapy.crawler import CrawlerProcess

class PostsSpider(scrapy.Spider):
    name = "com"
# def start_request(self):
    start_urls = [ 'https://mbasic.facebook.com/somoynews.tv/posts/3237170216376033' ]

# for url in urls:
#     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        page = response.url.split('/')[-1]

        html_file = 'com-%s.html' % page
        with open(html_file, 'wb') as f:
            f.write(response.body)

    # def parse(self, response):
    #     for post in response.css('div.post-item'):
    #         yield {
    #             'title': post.css('.post-header h2 a::text')[0].get(),
    #             'date': post.css('.post-header a::text')[1].get(),
    #             'author': post.css('.post-header a::text')[2].get()
    #
    #         }







        # for des in response.xpath("//div/p[@class='course-block__description']"):
        #     yield { 'des_text': des.xpath(".//div/p[@class='course-block__description']").extract_first()
        #             }
            # next_page= response.xpath("//li[@class='next']/a/@href").extract_first()
            # if next_page is not None:
            #     next_page_link= response.urljoin(next_page)
            #     yield scrapy.Request(url=next_page_link, callback=self.parse)