from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.spiders.lyrics import LyricsSpider

import os
from model.data_prep import prepare_data
from model.train_model import train_model
from model.test_model import test_model
from decouple import config

API_KEY = config('SECRET_KEY')

print('----------------------------')
print('     COLLECTING THE DATA    ')
print('----------------------------')
process = CrawlerProcess(get_project_settings())
process.crawl(LyricsSpider)
process.start()

print('----------------------------')
print('     TRAINING THE MODEL     ')
print('----------------------------')
train_df, test_df = prepare_data()
train_model(API_KEY, train_df)

print('----------------------------')
print('     TESTING THE MODEL      ')
print('----------------------------')
test_model(API_KEY, test_df)

print('----------------------------')
print('      PIPELINE FINISHED     ')
print('----------------------------')

while True:
    answer = input('Do you want to launch the application? [Y/N] ')
    if answer.lower().strip() == 'y':
        os.system('cmd /k "streamlit run main.py"')
    elif answer.lower().strip() == 'n':
        break
    else:
        pass