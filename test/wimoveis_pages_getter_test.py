import unittest

from ..app.wimoveis_pages_getter import WimoveisPagesGetter
from ..app.page_downloader import PageDownloader

class TestWimoveisPagesGetter(unittest.TestCase):

    def setUp(self):
        self.downloader = PageDownloader("https://www.wimoveis.com.br/apartamentos-venda-aguas-claras-df.html")
        self.page = self.downloader.downloadPage()
        self.pages_getter = WimoveisPagesGetter(self.page, "https://www.wimoveis.com.br/apartamentos-venda-aguas-claras-df.html")

    def test_get_pages(self):
        pages = self.pages_getter.GetPages()
        self.assertIs(type(pages), list)

    def test_transform_url(self):
        expectedUrl = "https://www.wimoveis.com.br/apartamentos-venda-aguas-claras-df-pagina-2.html"
        gotUrl = self.pages_getter._transform_url(2)
        self.assertEquals(expectedUrl, gotUrl)

if __name__ == '__main__':
    unittest.main(exit=False)