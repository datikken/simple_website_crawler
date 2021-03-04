import requests
from bs4 import BeautifulSoup

class Spider:
    def __init__(self, url):
        self.url_to_grab = url
        self.website_links = []
        self.clean_set_of_links = set()

    def grab_single_page_links(self):
        r = requests.get(self.url_to_grab)
        soup = BeautifulSoup(r.text, 'html.parser')
        soup_links = soup.findAll("a", href=True)
        links = []
        for soup_link in soup_links:
            links.append(soup_link["href"])
        return links

    def grab_all_pages_links(self):
        pages_links = self.grab_single_page_links()

        for page_link in pages_links:
           self.website_links.append(page_link)

    def normalize_links(self):
        unique_links = set(self.website_links)
        potential_trash_links = '#/'

        for trash in potential_trash_links:
            unique_links.remove(trash)

        for clean_link in unique_links:
            if not(clean_link.startswith('#')) or clean_link.startswith('javascript'):
                self.clean_set_of_links.add(clean_link)