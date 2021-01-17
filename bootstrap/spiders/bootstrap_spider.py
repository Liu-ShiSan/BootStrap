# -*- coding:utf-8 -*-
# !usr/bin/env python

import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BootStrapSpider(scrapy.Spider):
    name = "bootstrap"
    i = 1
    url_list = []
    txt = open(r'bootstrap\spiders\failed_url.txt', 'a+')
    with open(r'bootstrap\spiders\urls.txt') as f:
        for line in f:
            url_list.append(line)

    def start_requests(self):
        for i, url in enumerate(self.url_list):
            yield Request(url, callback=self.parse_process, meta={'index': i+1}, dont_filter=True)

    def parse_process(self, response):
        if response.status == 200:
            print("--正在保存代码..........")
            html = open('bootstrap/html/' + str(response.meta['index']) + '.html', 'a+', encoding='utf-8')
            print(response.text, file=html)
            print("--正在保存截图..........")
            self.web_normalise(response.url, response.meta['index'])
        else:
            self.txt.write(response.url + '\n')

    def web_normalise(self, url, index):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(url)
        # browser.set_window_size(1332, 1942)
        width = browser.execute_script("return document.documentElement.scrollWidth")
        height = browser.execute_script("return document.documentElement.scrollHeight")
        browser.set_window_size(width, height)
        browser.save_screenshot("bootstrap/screenshot/" + str(index) + ".png")
        browser.close()


if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl('bootstrap')
    process.start()
