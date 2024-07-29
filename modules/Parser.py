from bs4 import BeautifulSoup
import urllib.request


class Parser:
    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        request = urllib.request.urlopen(self.url)
        self.raw_html = request.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('li', class_='liga-news-item')

        for item in news:
            title = item.find('span', class_='d-block').get_text(strip=True)
            description = item.find('span', class_='name-dop').get_text(strip=True)
            href = self.url + item.find('a').get('href')
            self.results.append({
                'title': title,
                'description': description,
                'href': href
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            i = 1
            for item in self.results:
                file.write(
                    f'News №{i}\n\nНазвание: {item["title"]}\nОписание: {item["description"]}\nСсылка: {item["href"]}\n\n********\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
