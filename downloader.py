import requests

class Downloader:
    def download_html_page(self, url):
        user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) ''Gecko/20100101 Firefox/50.0')
        html = requests.get(url, headers={'User-Agent':user_agent}).text
        print(url)
        return
        # self.save_html_to_file(html)

    def save_html_to_file(self, text):
        file = open("./results/html/sample.html", "w")
        file.write(text)
        file.close()