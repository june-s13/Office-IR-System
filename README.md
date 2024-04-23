**FOR UNIT TEST (Run in root directory):** python -m unittest discover tests

**Features:** Web Crawler that utilizes Scrapy to download and store web documents, an indexer that uses Scikit-Learn to create an inverted index for efficient searching, and a query processor using Flask to handle and process user queries.    

**Starting the Web Crawler:**

cd webcrawler

scrapy crawl web_spider

**Creating the Index:**

python indexer.py

**Starting the Flask App:**

flask run

