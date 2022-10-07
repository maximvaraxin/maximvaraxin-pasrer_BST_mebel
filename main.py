from bs4 import BeautifulSoup
import requests
from config import configClass
from chromeDriverClass import chromeDriverClass

if __name__ == '__main__':

    if configClass.READ_XLS:
        catalogProducts = configClass.FILE_XLS.to_dict('records')

        for item in catalogProducts:
            configClass.DATABASE.insertProductName(str(item['name']))
    else:
        resultsDB = configClass.DATABASE.getProductName()
        requestObj = requests.get(configClass.URL, headers=configClass.HEADERS)
        bsObj = chromeDriverClass(configClass.URL)

        for resultDB in resultsDB:
            configClass.DATABASE.insertProductLinksDataBase(int(configClass.DATABASE.getWebID(resultDB)[0]), bsObj.getPageSearch(resultDB))

        reqs = configClass.DATABASE.getLink()

        for item in reqs:
            id = item[0]

            if item[1] != 'LinkIsNotFind':
                connect = requests.get(item[1])

                if connect:
                    soup = BeautifulSoup(connect.content, 'html.parser')

                    try:
                        width = soup.find("span", class_="js-changelable-props-val__SHIRINA").text
                        height = soup.find("span", class_="js-changelable-props-val__VYSOTA").text
                        depth = soup.find_all("span", class_="js-changelable-props-val__GLUBINA")[-1].text
                        matherial = soup.find("span", class_="js-attributes__set-value-text").text
                        status = 'В производстве'

                        configClass.DATABASE.upadteProductParamsDataBase(width, height, depth, matherial, status, id)

                    except:
                        width = 0
                        height = 0
                        depth = 0
                        matherial = 'Не указан'
                        status = 'Ошибка ссылки'

                        configClass.DATABASE.upadteProductParamsDataBase(width, height, depth, matherial, status, id)
            else:
                width = 0
                height = 0
                depth = 0
                matherial = 'Не указан'
                status = 'Снят с производства'

                configClass.DATABASE.upadteProductParamsDataBase(width, height, depth, matherial, status, id)

