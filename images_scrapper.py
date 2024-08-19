import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse, urljoin
import os
import colorama

colorama.init()
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE
RESET = colorama.Fore.RESET


pic_urls = set()
all_links = set()
visited_links = 0

def all_page_pics_urls(url):
    """Returns all internal links from website and ads pics url in pic_urls set"""
    internal_urls = set()
    domain_name = urlparse(url).netloc
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    r = requests.get(url, headers).content
    soup = bs(r, 'html.parser')
    for img in soup.findAll('img'):
        pic = img.attrs.get("src")
        img_link = urljoin(url, pic)
        parsed_img = urlparse(img_link)
        correct_url = parsed_img.scheme + "://" + parsed_img.netloc + parsed_img.path
        parsed_img = urlparse(correct_url)

        if correct_url not in pic_urls:
            if isinstance(parsed_img.path, str):
                if "." in parsed_img.path:
                    pic_urls.add(correct_url)
    
    for a in soup.find_all("a"):
        href = a.attrs.get('href')
        if href == "" or href is None:
            continue
        href = urljoin(url, href)

        parsed_href = urlparse(href)
        # удалить параметры URL GET, фрагменты URL и т. д.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if href in all_links:
            continue
        if domain_name in href and href not in internal_urls:
            internal_urls.add(href)
            all_links.add(href)

    return internal_urls

def pics_crawl(url, scan_limit):
    """Scans all internal links for pics and returns it in set"""
    global visited_links
    if visited_links == 0: print(f'{YELLOW}Идет сканнирование ссылок сайта...{RESET}')
    elif visited_links % 4 == 0: print(f'{YELLOW}...{RESET}')
    visited_links += 1
    links = all_page_pics_urls(url)
    for link in links:
        if visited_links > scan_limit:
            break
        pics_crawl(link, scan_limit=scan_limit)
    return pic_urls

def save_website_pics(url, scan_limit = 30):
    """Save all pics from website"""
    pics = list(pics_crawl(url, scan_limit=scan_limit))
    print(f'{BLUE}Сканирование завершено.{RESET}')
    name = urlparse(url).netloc
    path = os.path.join(os.getcwd(), name)
    print(f'{YELLOW}Создание папки для сохранения изображений...{RESET}')
    os.mkdir(path)
    print(f'{YELLOW}Загрузка изображений из сайта...{RESET}')
    saved_pic_count = 0
    for pic in pics:
        saved_pic_count += 1
        if saved_pic_count % 10 == 0: print(f'{YELLOW}...{RESET}')
        pic_name = urlparse(pic).path.split('/')[-1]
        with open(os.path.join(path, pic_name), "wb") as p:
            p.write(requests.get(pic).content)
    print(f"{GREEN}ЗАВЕРШЕНО. Кол-во сохраненных изображений: {saved_pic_count}{RESET}")

        
if __name__ == '__main__':   

    url = 'https://netology.ru'
    save_website_pics(url, scan_limit=15)