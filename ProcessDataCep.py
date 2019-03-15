from selenium import webdriver
import unittest
import json

class ProcessDataCep():
        driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        driver.get("http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm")

        for i in range(0,1):
                driver.find_element_by_xpath('//*[@id="Geral"]/div/div/span[2]/label/select').click()
                state = driver.find_element_by_xpath('//*[@id="Geral"]/div/div/span[2]/label/select/option[25]')
                driver.find_element_by_xpath('//*[@id="Geral"]/div/div/span[2]/label/select/option[25]').click()
                driver.find_element_by_xpath('//*[@id="Geral"]/div/div/div[4]/input').click()



                table = []
                columns = []
                values = {}
                valuesTable = []
                while len(valuesTable) <= 100:
                        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]").is_displayed()

                        if elem:
                                table = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]")
                        else:
                                table = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table")
                        columns = (table.find_elements_by_tag_name('td'))

                        for index in range(0, len(columns), 4):
                                values.update({"Location":columns[index].text})
                                values.update({"CepsRange":columns[index + 1].text})
                                valuesTable.append(values)
                                values = {}
                                if len(valuesTable) == 100:
                                        break
                        columns = []
                        table = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]/a").click()



                dicDad = {'1':valuesTable}
                file = open('result.json', 'w')
                json.dump(dicDad, file)
                driver.close();

if __name__ == '__main__':
    unittest.main