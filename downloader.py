import requests

class Downloader:
    def __init__(self, array_of_links):
        self.array_of_links = array_of_links

    def download_html_page(self):
        html = requests.get(self.array_of_links).text
        self.save_html_to_file(html)

    def save_html_to_file(self, text):
        file = open("./results/html/sample.html", "w")
        file.write(text)
        file.close()