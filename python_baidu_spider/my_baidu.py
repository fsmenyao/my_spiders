from urllib import request, parse
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os


headers = {"Accept": "text/html, application/xhtml+xml, image/jxr, */*",
         "Accept - Encoding": "gzip, deflate, br",
         "Accept - Language": "zh - CN",
         "Connection": "Keep - Alive",
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
         "referer": "baidu.com"}

cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))

headall=[]
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders=headall
urllib.request.install_opener(opener)

csvfile_names = os.listdir('.\\URL_BAIDU_CSV_A')

txtfile = open('baidu_results.txt', 'a+', encoding='utf-8')

for csvfile_name in csvfile_names:
    stock_name = csvfile_name.split('.')[0]
    stock_name = stock_name.split('_')[-1]
    txtfile.write(stock_name)
    txtfile.write('\n')
    txtfile.flush()

    csvfile_path = '.\\URL_BAIDU_CSV_A\\' + csvfile_name
    # print(csvfile_path)
    csvfile = pd.read_csv(csvfile_path, encoding='unicode_escape', sep='\n')
    urls_np = csvfile.values
    urls = [url[0] for url in urls_np]

    for i, url in enumerate(urls):
        print(url)
        txtfile.write(str(url) + '\n')
        txtfile.flush()
        data = urllib.request.urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(data, 'html.parser')
        results = soup.find_all('div', id='header_top_bar')
        for result in results:
            content = result.select('span')[0].get_text()
            content_str = content.strip()
            txtfile.write(content_str + '\n')
            txtfile.flush()
        time.sleep(3 + 1*random.random())
txtfile.close()
