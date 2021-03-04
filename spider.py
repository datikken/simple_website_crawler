import requests
from bs4 import BeautifulSoup

class Spider:
    def __init__(self, url):
        self.url_to_grab = url
        self.website_links = []
        self.clean_set_of_links = set()
        self.user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) ''Gecko/20100101 Firefox/50.0')

    def get_clean_links(self):
        return self.clean_set_of_links

    def grab_single_page_links(self):
        r = requests.get(self.url_to_grab, headers={'User-Agent':self.user_agent})
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
        unique_links = list(self.website_links)

        needles = '(#*'

        for link in unique_links:
            for needle in needles:
                if needle in link:
                    unique_links.remove(link)

        self.clean_set_of_links = set(unique_links)

        result = list(self.clean_set_of_links)
        n = len(self.clean_set_of_links)

        def sort_array_by_element_length(s, n):
            for i in range(1, n):
                temp = s[i]

                j = i - 1
                while j >= 0 and len(temp) < len(s[j]):
                    s[j + 1] = s[j]
                    j -= 1

                s[j + 1] = temp

        sort_array_by_element_length(result, n)

        for link in result:
            print(link)