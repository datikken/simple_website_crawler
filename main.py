from spider import *
from downloader import *

base_url = 'http://t1167801.tmpl24.ru/'

spider = Spider(base_url)
spider.grab_all_pages_links()
spider.normalize_links()

# links = spider.get_clean_links()

# print(links)

# downloader = Downloader()

# for link in links:
#     link_to_parse = base_url + link
#     downloader.download_html_page(link_to_parse)