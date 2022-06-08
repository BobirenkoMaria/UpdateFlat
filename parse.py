from bs4 import BeautifulSoup
import requests

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70',
           'accept': '*/*'}

info = []

def get_html(url, params=None):
    try:
        r = requests.get(url, headers=HEADERS, params=params)
    except requests.exceptions.ConnectionError:
        return None
    return r


def get_url(website, flat_num=None):
    url = ''

    if website == 0:
        url = 'https://ciox.ru/check-user-agent'
    elif website == 1:
        url = 'https://sabaneeva22a.ru/flat-info/?' + str(flat_num)
    elif website == 2:
        url = ''
    return url


def get_content(html, website):
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find('li', class_='p10__flat-price')

    info.append({
        'price': (price.get_text())[10:-5]
    })

    # print(info)


def parse(start_line, end_line):
    start_line1 = start_line - 1
    count = end_line - start_line
    i=1
    while start_line1 < (end_line-1):
        website = 1
        URL = get_url(website, start_line1)

        html = None
        while html == None:
            html = get_html(URL)
            try:
                if html.status_code == 200:
                    get_content(html.text, website)
                    start_line1 += 1

                    print(str(round(i*100/count)) + '%')
                    i+=1

            except AttributeError:
                print("Connetction refused")

    return info