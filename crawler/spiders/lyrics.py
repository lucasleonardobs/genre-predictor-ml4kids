import scrapy
from crawler.items import MusicLyric

class LyricsSpider(scrapy.Spider):
  name = 'lyrics'
  start_urls = ['https://www.letras.mus.br']

  custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'data/raw_data.csv'
    }

  def parse(self, response):
    url_rap = 'https://www.letras.mus.br/top.html?genre=64&slug=hip-hop-rap&period=5&page=top#Sempre'
    url_sertanejo = 'https://www.letras.mus.br/top.html?genre=64&slug=sertanejo&period=5&page=top#Sempre'
    url_funk = 'https://www.letras.mus.br/top.html?genre=64&slug=funk&period=5&page=top#Sempre'

    yield scrapy.Request(url_rap, callback=self.parse_lyric_link)
    yield scrapy.Request(url_sertanejo, callback=self.parse_lyric_link)
    yield scrapy.Request(url_funk, callback=self.parse_lyric_link)

  def parse_lyric_link(self, response):
    links = response.css('ol.top-list_mus li a::attr(href)').getall()[:300]
    for link in links:
      yield scrapy.Request(f"https://www.letras.mus.br{link}", callback=self.parse_lyric)

  def parse_lyric(self, response):
    check_language_lyric = response.css('a.lyric_event.lm_lang::text').get()

    if not check_language_lyric:
      title = response.css('h1::text').get()
      artist = response.css('h2 span::text').get()
      lyric = response.css('div.cnt-letra p::text').getall()
      genre = response.css('span:nth-of-type(2) span::text').get()

      music_lyric = MusicLyric(
        title = title,
        artist = artist,
        lyric = lyric,
        genrer = genre
      )

      yield music_lyric