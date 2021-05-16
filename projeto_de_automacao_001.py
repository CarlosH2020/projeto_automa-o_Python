from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import pyautogui as py
import time

# Url que vai ser usada...
url = 'https://www.mercadobitcoin.com.br/'
driver = webdriver.Chrome()


def chamada_driver():
    driver.get(url)
    # Usando o Xpath para extrair valores..
    btc = driver.find_element_by_xpath('/html/body/section[1]/div/div[2]/div/div/div[2]/div[2]').text
    xrp = driver.find_element_by_xpath('/html/body/section[1]/div/div[2]/div/div/div[3]/div[1]/div/div[2]').text
    moedas = [btc, xrp]
    for moeda in moedas:
        print('=' * 46)
        print(moeda)
        print('=' * 46)


if __name__ == '__main__':
    py.alert(text='Bora começar?', title='Analise de criptomoedas', button='OK')
    chamada_driver()
    time.sleep(3)
    py.click(x=1027, y=19)








