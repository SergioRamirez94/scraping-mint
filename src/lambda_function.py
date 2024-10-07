import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from grid_india.spiders.india_spider import GridSpider

def lambda_handler(event, context):
    process = CrawlerProcess(get_project_settings())
    
    process.crawl(GridSpider)
    process.start()
    return {
        'statusCode': 200,
        'body': 'Spider ejecutado exitosamente'
    }