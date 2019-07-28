import scrapy

class find(scrapy.Spider):
	name='activity_scraper'
	start_urls=['file:///C:/Users/DELL.india/AppData/Local/Temp/activity.html']

	def parse(self,response):
		for outer in response.xpath("//div[@class='outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp']"):
			yield{
			'content':outer.xpath(".//div[@class='mdl-grid']/div[@class='content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1']/a/text()").extract(),
			'time':outer.xpath(".//div[@class='mdl-grid']/div[@class='content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1']/text()").extract(),
			}