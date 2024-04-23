import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class WebSpider(scrapy.Spider):
    name = "web"

    def __init__(self, seed_url, max_pages=None, max_depth=None, *args, **kwargs):
        super(WebSpider, self).__init__(*args, **kwargs)
        self.start_urls = [seed_url]
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.crawled_count = 0

    def parse(self, response):
        if self.max_pages and self.crawled_count >= self.max_pages:
            return
        self.crawled_count += 1
        filename = f"output/{response.url.split('/')[-1]}.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        for a in response.css('a::attr(href)'):
            yield response.follow(a, self.parse)

# To run the spider with command-line inputs
if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(WebSpider, seed_url="http://example.com", max_pages=100, max_depth=3)
    process.start()
