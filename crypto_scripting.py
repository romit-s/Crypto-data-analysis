from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from ..general_utility import get_hash_of_html
# from ..s3_upload import hash_check
import hashlib
import json
from urllib.request import urlopen as uReq

import time


import json



def to_json(entity):
    hash_obj = json.dumps(entity)
    with open("crypto_data.json", "w") as ts:
        ts.write(hash_obj)



def get_data():

    try:
        PATH = "C:\\Users\\91702\\Downloads\\chromedriver_win32\\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(PATH, options=options)
        driver.maximize_window()
        driver.get("https://coincodex.com/crypto/bitcoin/historical-data/")
        time.sleep(5)

        data_list = []

        try:
            dates = driver.find_elements(By.XPATH,'/html/body/app-root/app-root/div/div/div/div[1]/app-coin-history-data/section[2]/div/table/tbody/tr/td[1]')
            btc_open = driver.find_elements(By.XPATH,'/html/body/app-root/app-root/div/div/div/div[1]/app-coin-history-data/section[2]/div/table/tbody/tr/td[2]')
            btc_close = driver.find_elements(By.XPATH,'/html/body/app-root/app-root/div/div/div/div[1]/app-coin-history-data/section[2]/div/table/tbody/tr/td[3]')
            for i in range(len(dates)):
                data_dict = {}
                try:
                    data_dict["date"] = dates[i].text

                    data_dict["btc_open"] = int(btc_open[i].text[2:].replace(",",""))
                    # print(data_dict)
                    data_dict["btc_close"] = int(btc_close[i].text[2:].replace(",",""))
                    data_list.append(data_dict)
                except Exception:
                    pass

        except Exception:
            pass
        driver.get("https://coincodex.com/crypto/ethereum/historical-data/")
        time.sleep(5)



        try:
            eth_open = driver.find_elements(By.XPATH,'/html/body/app-root/app-root/div/div/div/div[1]/app-coin-history-data/section[2]/div/table/tbody/tr/td[2]')
            eth_close = driver.find_elements(By.XPATH,'/html/body/app-root/app-root/div/div/div/div[1]/app-coin-history-data/section[2]/div/table/tbody/tr/td[3]')
            # print(len(eth_open))
            for i in range(len(eth_open)):

                try:
                    # print(eth_open[i].text)

                    data_list[i]["eth_open"] = float(eth_open[i].text[1:].replace(',', ''))
                    data_list[i]["eth_close"] = float(eth_close[i].text[1:].replace(',', ''))
                    # print(data_list[i])

                except Exception:
                    pass

        except Exception:
            pass


        driver.quit()
    except Exception:
        pass



    return data_list


if __name__ == "__main__":
    data_list3 = get_data()
    to_json(data_list3)
    print(data_list3)
    print(len(data_list3))
