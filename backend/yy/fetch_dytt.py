import requests
from pony.orm import db_session
from bs4 import BeautifulSoup as bsp
import re
from model import Film

site = 'http://www.ygdy8.net'


def getSoup(url):
    r = requests.get(url)
    r.encoding = 'gb18030'
    return bsp(r.text, "html.parser")


@db_session
def filterMovie(url):
    resultList = []
    soup = getSoup(url)
    tables = soup.find_all('table', class_='tbspan')
    for table in tables:
        nameA = table.find('a', text=re.compile("《"))
        td = table.find('td', text=re.compile("IMD"))
        if td is not None:
            scoreStr = re.findall(r"评分 (.+?)/10", td.text)
            if (len(scoreStr) > 0):
                try:
                    score = float(scoreStr[0])
                    if (score > 8):
                        name = nameA.text
                        url = site + nameA['href']
                        print('url:', url)
                        print('title:', name)
                        print('score:', score)
                        downloadLink = getDownloadLink(url)
                        print('link:', downloadLink)
                        try:
                            film = Film(
                                cn_name=name,
                                en_score=str(score),
                                download_link=downloadLink)
                            resultList.append(film)
                        except Exception as e:
                            print('.....', e)

                except:
                    print('error !!')
    return resultList


def getDownloadLink(url):
    soup = getSoup(url)
    downloadTd = soup.find('td', attrs={"style": "WORD-WRAP: break-word"})
    downloadA = downloadTd.find('a')
    return downloadA['href']


def getPageResource(url):
    resultList = filterMovie(url)
    if len(resultList) > 0:
        print("result: ", resultList)


if __name__ == '__main__':
    for index in range(156):
        index += 1
        url = 'http://www.ygdy8.net/html/gndy/oumei/list_7_' + \
            str(index) + '.html'
        getPageResource(url)
