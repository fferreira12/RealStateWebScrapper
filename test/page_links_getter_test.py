import unittest

from ..app.page_downloader import PageDownloader
from ..app.page_links_getter import PageLinksGetter

class TestPageLinksGetter(unittest.TestCase):

    def setUp(self):
        self.url = "http://www.wimoveis.com.br/apartamentos-venda-aguas-claras-df.html"
        self.page_downloader = PageDownloader(self.url)
        page = self.page_downloader.downloadPage()
        self.pages_links_getter = PageLinksGetter(page, {"class": "aviso"})

    def test_get_elements(self):
        elements = self.pages_links_getter.get_elements()
        self.assertIsNotNone(elements, "Page retrieved should not be none")
        self.assertEquals(len(elements), 20)

if __name__ == '__main__':
    unittest.main(exit=False)
