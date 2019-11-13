import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    bs = BeautifulSoup(html, 'lxml')
    data = []
    job_list = bs.find('div', id='pjax-job-list').find_all('div', class_='card card-hover card-visited wordwrap job-link')

    for item in job_list:
        try:
            title = item.find('h2', class_='add-bottom-sm').text
            company = item.find('b').text
            descr = item.find('p', class_='overflow').text
            url = 'https://www.work.ua' + item.find('h2', class_='add-bottom-sm').find('a').get('href')

            data.append({'title': title, 'company': company, 'descr': descr, 'url': url})
        except:
            pass
    print(data)


def main():
    pattern = 'https://www.work.ua/ru/jobs-kyiv-python/?page={}'

    for i in range(0, 4):
        url = pattern.format(str(i))
        get_data(get_html(url))


if __name__ == "__main__": main()
