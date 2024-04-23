import unittest
from unittest.mock import patch
from scrapy.http import HtmlResponse
from webcrawler.webcrawler.spiders.web_spider import WebSpider

class TestWebCrawler(unittest.TestCase):
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_parse_function(self, mock_open):
        spider = WebSpider(seed_url="http://example.com", max_pages=1, max_depth=1)
        mock_response = HtmlResponse(url='http://example.com', body=b"<html></html>", encoding='utf-8')
        result = list(spider.parse(mock_response))
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
