import urllib.request
import ssl
import httplib2
from bs4 import BeautifulSoup

links = []

main_link = "your_link_here"



def save_file(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    name = url.split('/')[7]
    print(name)
    urllib.request.urlretrieve(url, "images/%s" %name)


def find_images(url_to_site):
    http = httplib2.Http()
    response, content = http.request(url_to_site)

    for link in BeautifulSoup(content).find_all('a', href=True):
        
        linko = link["href"]
        
        if linko.endswith(".png") or linko.endswith(".jpg"):
            if 'x' not in linko:
                links.append(linko)
        



if __name__ == "__main__":
    find_images(main_link)
    print(len(links))
    for link in links:
        save_file(main_link + link)