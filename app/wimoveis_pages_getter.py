from bs4 import BeautifulSoup
import math

from pages_getter import PagesGetter


class WimoveisPagesGetter(PagesGetter):

    def __init__(self, pageHtmlStr, firstPageUrl):
        self.pageHtmlStr = pageHtmlStr
        self.firstPageUrl = firstPageUrl
        self.page = BeautifulSoup(pageHtmlStr, 'lxml')

    def GetPages(self):
        val = [self._transform_url(x) for x in range(1,self._get_total_pages()+1)]
        return val

    def _get_total_pages(self):
        total_items = int(self.page.find_all("h1")[0].find("strong").contents[0].replace(".", ""))
        total_pages = total_items / 20
        if not total_pages.is_integer():
            total_pages = math.trunc(total_pages) + 1
        return total_pages

    def _transform_url(self, pageNumber):
        if pageNumber == 1:
            return self.firstPageUrl
        return self.firstPageUrl[:-5]+"-pagina-"+str(pageNumber)+self.firstPageUrl[-5:]

