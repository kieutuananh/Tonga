from flask import Flask, render_template
app = Flask(__name__)


import requests
from bs4 import BeautifulSoup

BASE_ULR = 'https://tiki.vn/laptop/c8095?src=c.8095.hamburger_menu_fly_out_banner'

app = Flask(__name__)


def get_url(URL):
    """Get HTML from URL
    """
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

    

def crawl_tiki(URL):
    soup = get_url(URL)
    contents = soup.find_all('div', class_='product-item')
    data = []
    for content in contents:
        d = {'image':'', 'title':'', 'final_price':'', 'link':''}
        try:
            d['image'] = content.find('img', class_="product-image")['src']
            d['title']= content.find('a', class_='')['title']
            d['final_price'] = content.find('span', class_='final-price').text.strip()
            d['link'] = content.find('a', class_='')['href']
        except:
            pass
        data.append(d)
    return data


@app.route('/')
def home():
    data = crawl_tiki(BASE_ULR)
    return render_template('home.html', data=data)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 