from selenium import webdriver
import unittest
import json

class ProcessDataCep():
        driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        driver.get("http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm")
        dicDad = {}

        for i in range(0,2):
                driver.find_element_by_xpath('//*[@id="Geral"]/div/div/span[2]/label/select').click()

                if i == 0:
                        state = 'SC'
                        driver.find_element_by_xpath('//*[@id="Geral"]/div/div/span[2]/label/select/option[25]').click()
                else:
                        state = 'SP'
                        driver.find_element_by_xpath('//*[@id="Geral"]/div/div/span[2]/label/select/option[27]').click()
                driver.find_element_by_xpath('//*[@id="Geral"]/div/div/div[4]/input').click()



                table = []
                columns = []
                values = {}
                valuesTable = []
                count = 0
                while valuesTable.__len__() != 100:

                        if count == 0:
                                table = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]")
                        else:
                                table = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table")
                        columns = (table.find_elements_by_tag_name('td'))

                        count += 1

                        for index in range(0, columns.__len__(), 4):
                                values.update({"Location":columns[index].text})
                                values.update({"CepsRange":columns[index + 1].text})
                                valuesTable.append(values)
                                values = {}
                                if valuesTable.__len__() >= 100:
                                        break
                        columns = []
                        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]/a").click()



                driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[6]/a").click()

                dicDad.update({state:valuesTable})
        file = open('resultSelenium.json', 'w')
        json.dump(dicDad, file)
        driver.close();


if __name__ == '__main__':
    unittest.main