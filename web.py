import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
url = "https://www.acmicpc.net/source/61927657" 
res = requests.get(url, headers=headers)
res.raise_for_status() # 정상 200


soup = BeautifulSoup(res.text, "lxml")
Codebox = soup.find('ol', attrs={"class": "CodeMirror-lines"})
Codes = Codebox.find_all('a')