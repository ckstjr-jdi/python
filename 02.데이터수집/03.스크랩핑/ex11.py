import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


def scrap(section):
    url = f'https://news.naver.com/section/{section}'
    soup = create_soup(url)
    news_head = soup.find('ul', attrs={'class':'sa_list'})
    li = news_head.find_all('li', limit=5)
    for idx, item in enumerate(li):
        title = item.find('strong', attrs={'class':'sa_text_strong'}).getText()
        link = item.find('a')['href']
        print('-'*70)
        print(idx+1, title)
        print(link)
        print('-'*70)
        
if __name__=="__main__":
    while True:
        section = input('경제:101|사회:102|생활/문화:103|>')
        if section == '': break
        scrap(section)