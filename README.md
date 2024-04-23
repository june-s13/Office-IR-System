[For UNIT TEST (Run in root directory): python -m unittest discover tests]

Features:  
Web Crawler: Utilizes Scrapy to download and store web documents.
Indexer: Uses Scikit-Learn to create an inverted index for efficient searching.
Query Processor: A Flask application that handles and processes user queries.

Starting the Web Crawler:
cd webcrawler
scrapy crawl web_spider

Creating the Index:
python indexer.py

Starting the Flask App:
flask run

