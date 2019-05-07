from bs4 import BeautifulSoup
import html5lib

from page_downloader import PageDownloader
from wimoveis_pages_getter import WimoveisPagesGetter


class PageLinksGetter():

    def __init__(self, page, selecting_attributes):
        self.page = page
        self.selecting_attributes = selecting_attributes

    def get_elements(self):
        soup = BeautifulSoup(self.page, 'lxml')
        items = soup.find_all(attrs=self.selecting_attributes)
        return items

    def setPage(self, page):
        self.page = page


def GetAllPageLinks(url):
    page_downloader = PageDownloader(url)
    page = page_downloader.downloadPage()
    pages_getter = WimoveisPagesGetter(page, url)
    return pages_getter.GetPages()