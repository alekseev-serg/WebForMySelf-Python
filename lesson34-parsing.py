from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.ua-football.com'
request = urllib.request.urlopen('https://www.ua-football.com/sport')
html = request.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_='liga-news-item')

result = []
for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    description = item.find('span', class_='name-dop').get_text(strip=True)
    href = url + item.find('a').get('href')
    result.append({
        'title': title,
        'description': description,
        'href': href
    })

print(result)

f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in result:
    f.write(f'News №{i}\n\nНазвание: {item["title"]}\nОписание: {item["description"]}\nСсылка: {item["href"]}\n\n********\n')
    i += 1
