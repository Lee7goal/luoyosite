import requests
from bs4 import BeautifulSoup as bs


def get_data(link, page):

    data = {
        'page': page,
        'total': 30
    }

    res = requests.get(link, data)
    tmp_html = res.json()['data']['html']
    soup = bs(tmp_html, 'lxml')

    app_list = soup.find_all(name='div', attrs={'class': 'taptap-top-card'})
    for app in app_list:
        app_icon_url = app.find(name='a', attrs={'class': 'card-left-image'}).find('img').get('src')
        app_name = app.find(name='a', attrs={'class': 'card-middle-title'}).get_text().replace('\n', '').\
            replace('（测试版）', '').replace('（测试服）', '').strip()
        app_url = app.find(name='a', attrs={'class': 'card-middle-title'}).get('href')
        app_author = app.find(name='p', attrs={'class': 'card-middle-author'}).get_text().replace('\n', '').strip().\
            replace('\xa0', '')
        app_point = app.find(name='p', attrs={'class': 'middle-footer-rating'}).get_text().replace('\n', '').strip()
        app_description = app.find(name='p', attrs={'class': 'card-middle-description'}).get_text().replace('\n', '').\
            strip()
        app_tag = app.find(name='div', attrs={'class': 'card-middle-category'}).get_text().replace('\n', '').strip()
        yield([
            app_name,
            app_url,
            app_author,
            app_point,
            app_description,
            app_tag,
            app_icon_url
        ])
