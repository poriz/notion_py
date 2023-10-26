from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
# https://news.naver.com/main/list.naver?mode=LS2D&<sid2=259>&mid=shm&sid1=101&date=20230915&page=1
# sid2 = 경제 하위탭
# date, page 변수
class c_data:
    def __init__(self):
        self.tab_list = ['259']
        self.my_time = datetime.now().strftime("%Y%m%d")
        self.contents = []
    def run_code(self):
        for tab in self.tab_list:
            for pg in range(1,11):
                url = f'https://news.naver.com/main/list.naver?mode=LS2D&sid2={tab}&mid=shm&sid1=101&date={self.my_time}&page={pg}'
                res = urlopen(url)
                soup = BeautifulSoup(res.read(), 'lxml')
                titles = soup.select('.type06_headline > li > dl > dt:nth-child(2) > a')
                for i in range(len(titles)):
                    title = titles[i].get_text().strip()
                    source = titles[i].attrs['href']
                    self.contents.append((title,source))
        return self.contents
