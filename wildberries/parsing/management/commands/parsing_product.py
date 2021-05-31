from django.core.management.base import BaseCommand
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from parsing.models import Product

class Command(BaseCommand):
    help = 'Wildberries parser'

    def handle(self, *args, **kwargs):
        self.stdout.write("Идёт процесс парсинга...")
        ua = dict(DesiredCapabilities.FIREFOX)
        options = webdriver.FirefoxOptions()
        options.set_headless() 


        driver = webdriver.Firefox(firefox_options=options)

        for i in range(1, 10):
            driver.get(f'https://www.wildberries.ru/brands/marks-and-spencer/all?page={i}')
            time.sleep(10)
            
            for f in range(1, 100 + 1):
                prod = driver.find_element_by_xpath(f'//*[@id="catalog-content"]/div[4]/div[{f}]/div')
                Product.objects.create(product= prod.text)
        self.stdout.write("Готово")