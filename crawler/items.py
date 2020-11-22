from scrapy.item import Item, Field

class MusicLyric(Item):
  title = Field()
  artist = Field()
  lyric = Field()
  genrer = Field()
