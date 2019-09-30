import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'fitness'
    page_number = 2
    start_urls = [
         'https://www.jefit.com/exercises/bodypart.php?id=11&exercises=All'
    ]

    def parse(self, response):
        items = QuotetutorialItem()

        container = response.css('td.MiddleColumn')

        for name in container :
            title = name.css('h4 a::attr(href)').extract()
            muscle = name.css('h4+p::text').extract()
            equipmentType = name.css('p~p+p::text').extract()

            items['title'] = title
            items['muscle'] = muscle
            items['equipmentType'] = equipmentType

            yield items


        next_page = './bodypart.php?id=11&exercises=All&All=0&Bands=0&Bench=0&Dumbbell=0&EZBar=0&Kettlebell=0&MachineStrength=0&MachineCardio=0&Barbell=0&BodyOnly=0&ExerciseBall=0&FoamRoll=0&PullBar=0&WeightPlate=0&Other=0&Strength=0&Stretching=0&Powerlifting=0&OlympicWeightLifting=0&Beginner=0&Intermediate=0&Expert=0&page=+ str(QuoteSpider.page_number) +'
        if QuoteSpider.page_number <= 130:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)