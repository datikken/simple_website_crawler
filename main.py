from spider import *
from downloader import *

url = 'http://t1167801.tmpl24.ru/'
another_one = 'http://jsux.fun'

spider = Spider(url)
spider.grab_all_pages_links()
spider.normalize_links()

downloader = Downloader(url)
downloader.download_html_page()