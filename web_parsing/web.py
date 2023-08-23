# import requests
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
# url = "https://points.jshsus.kr/get_maeso?stuid=1101" 
# res = requests.get(url, headers=headers)
# res.raise_for_status() # 정상 200


# soup = BeautifulSoup(res.text, "lxml")
# Codebox = soup.find('ol', attrs={"class": "CodeMirror-lines"})
# Codes = Codebox.find_all('a')

# html = urlopen(url)
# object = BeautifulSoup(html, "html.parser")

basicUrl = "https://points.jshsus.kr/get_maeso?stuid="

result = []

def search_meso(start, end):
    global result
    for i in range(start, end+1): #마지막 번호
        url = basicUrl + str(i)
        html = urlopen(url)
        object = BeautifulSoup(html, "html.parser")
        result.append([object, i])
        print([object, i])


#1학년
search_meso(1101, 1120)
search_meso(1201, 1220)
search_meso(1301, 1320)
search_meso(1401, 1420)

#2학년
search_meso(2101, 2121)
search_meso(2201, 2221)
search_meso(2301, 2321)
search_meso(2401, 2420)

df = pd.DataFrame(data=result,columns=['maeso', 'student'])
df.to_csv('jshs_points.csv', index=False, encoding='cp949')