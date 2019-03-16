# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
import json



class DataSpider(Spider):
    name = 'data'
    start_urls = ('http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm',)
    dic = {}
    jsonDad = []
    state = 'SC'

    def parse(self, response):
            token = response.xpath('//*[@value="Buscar"]/@value').extract_first()
            return FormRequest.from_response(response,
                                              formdata={'Buscar': token,
                                                        'UF': self.state},
                                              callback=self.scrape_pages)
            
        

    def scrape_pages(self, response):
        test = response.xpath('//table//td//text()').getall()
        return FormRequest.from_response(response, self.organization(test))
        
    def organization(self, values):
        i = 2
        x = 3
        for item in values:
            if i < 198 and x < 198:
                textEcode = values[i]
                textEcode.encode("utf-8")
                self.dic.update({textEcode: values[x]})
                x += 4
                i += 4
        self.jsonDad.append(self.dic)
        file = open('resultScrapySC.json', 'w')
        json.dump(self.jsonDad, file)


