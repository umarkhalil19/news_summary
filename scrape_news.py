import requests
from bs4 import BeautifulSoup

def search_news(keyword, max_pages):
    # url = f"https://www.detik.com/search/searchall?query={keyword}&siteid=2&source_kanal=true"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    # response = requests.get(url, headers=headers)
    
    # if response.status_code != 200:
    #     print("Error:", response.status_code)
    #     return []

    # soup = BeautifulSoup(response.text, 'html.parser')
    # articles = soup.find_all('article', class_='list-content__item')

    news_list = []

    for page in range(max_pages):
        url = f"https://www.detik.com/search/searchall?query={keyword}&page={page}&result_type=relevansi"

        response = requests.get(url, headers=headers)
    
        if response.status_code != 200:
            print("Error:", response.status_code)
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='list-content__item')

        for article in articles:
            title = article.find('h3', class_='media__title').get_text()
            link = article.find('a')['href']
            time = article.find('div', class_='media__date').get_text()
            
            news_list.append({
                'title': title,
                'link': link,
                'time': time
            })

    return news_list

keyword = input("Masukkan kata kunci berita: ")
max_pages = int(input("Masukkan jumlah halaman yang ingin diambil: "))
news = search_news(keyword, max_pages)

# print(news);

for idx, article in enumerate(news):
    print(f"{idx + 1}. {article['title']}")
    print(f"Waktu Terbit {article['time']}")
    print(f"Link: {article['link']}\n")