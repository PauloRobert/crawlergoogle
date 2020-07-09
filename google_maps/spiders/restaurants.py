# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from shutil import which
import time
from scrapy import Selector
from selenium.webdriver.common.keys import Keys


class RestaurantsSpider(scrapy.Spider):
    name = 'restaurants'
    allowed_domains = ['google.com']
    start_urls = ['https://google.com']

    search_option = input("Enter your search option : ")

    def parse(self, response):
        chrome_path = which('chromedriver')
        driver = webdriver.Chrome(executable_path=chrome_path)
        driver.maximize_window()
        driver.get("https://www.google.com")
        search_box = driver.find_element_by_xpath(
            "//input[@class='gLFyf gsfi']")
        search_box.send_keys(''' %s ''' % self.search_option)
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)
        more_places = driver.find_element_by_xpath("//span[@class='i0vbXd']")
        more_places.click()
        time.sleep(2)

        shop = driver.find_elements_by_xpath("//div[@class='dbg0pd']")
        while True:
            shop = driver.find_elements_by_xpath("//div[@class='dbg0pd']")
            for x in shop:
                x.click()
                x.click()
                time.sleep(6)
                html = driver.page_source
                resp = Selector(text=html)
                yield{
                    'Name': resp.xpath("//div[@class='SPZz6b']/div/span/text()").get(),
                    'Website': resp.xpath("(//a[@class='CL9Uqc ab_button']/@href)[1]").get(),
                    'Address': resp.xpath("//span[@class='LrzXr']/text()").get(),
                    'Evaluation': resp.xpath("//div/span[@class='Aq14fc']/text()").get(),
                    'Hours': resp.xpath("//tr[@class='K7Ltle']/td[2]/text()").get(),
                    'Telephone': resp.xpath("//span[@data-dtype='d3ifr']/span/text()").get(),
                }
            next_page = driver.find_element_by_xpath(
                "//a[@class='G0iuSb' and @id='pnnext']")
            next_page.click()
            time.sleep(5)

        time.sleep(6)
        driver.close
