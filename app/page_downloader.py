from urllib.request import urlopen, Request
import urllib
import ssl

from publisher import Publisher


class PageDownloader(Publisher):

    def __init__(self, url):
        self.url = url
        self.subscribers = []

    def setUrl(self, url):
        self.url = url

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def downloadPage(self):
        html = ""
        page = ""
        try:
            request = Request(self.url)
            request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
            html = urlopen(request)
            page = self.decodePage(html)
            self.emit(page)
        except urllib.error.URLError as e:
            print("Could not fetch the page")
        return page

    def decodePage(self, response):
        html_response = response.read()
        encoding = response.headers.get_content_charset('utf-8')
        decoded_html = html_response.decode(encoding)
        return decoded_html

    def emit(self, data):
        for sub in self.subscribers:
            sub.onNewPage(data)