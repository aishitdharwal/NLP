import scrapy

class find(scrapy.Spider):
	name='name'
	start_urls=['file:///C:/Users/DELL.india/AppData/Local/Temp/a.html']

	def parse(self,response):
		for head in response.xpath("//div[@class='head']"):
			yield{
			'time':head.xpath(".//div[@class='shead']/text()").extract(),
			'content':head.xpath(".//div[@class='shead']/a/text()").extract(),
			}