from django.core.management.base import BaseCommand
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from parsing.models import Product

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        '''time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        Product.objects.create(product='test')'''
        ua = dict(DesiredCapabilities.FIREFOX)
        options = webdriver.FirefoxOptions()
        options.set_headless() 


        driver = webdriver.Firefox(firefox_options=options)

        driver.get('https://www.wildberries.ru/brands/marks-and-spencer/all?fkind=2&sort=popular&bid=450a8a63-dab7-4c97-8f69-3991071e689d')

        time.sleep(10)

        #product = driver.find_element_by_xpath('//*[@id="catalog-content"]/div[4]/div[1]/div')

        for i in range(1, 100 + 1):
            prod = driver.find_element_by_xpath(f'//*[@id="catalog-content"]/div[4]/div[{i}]/div')
            Product.objects.create(product= prod.text)