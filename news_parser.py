import requests
from bs4 import BeautifulSoup
import json

def get_html():
    url = 'https://www.bbc.com/news'
    r = requests.get(url)
    return r.text


def get_news():
    html = get_html()
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('div', class_='gs-c-promo')
    return news


def main():
    news = get_news()
    articles = []
    for item in news:
        article = {}
        link = item.find('a', class_='gs-c-promo-heading')
        article['header'] = link.find('h3').text
        describe = item.find('p')
        if describe:
            article['describe'] = describe.text
        article['href'] = link.get('href')
        try:
            category_link = item.find('a', class_='gs-c-section-link').find('span').text
        except:
            category_link = None
        article['category'] = category_link
        time = item.find('time')
        if time:
            article['time'] = time.get('datetime')
        articles.append(article)
    with open('news.json', 'w') as file:
        json.dump(articles, file, indent=2, ensure_ascii=False)



if __name__ == '__main__':
    main()
