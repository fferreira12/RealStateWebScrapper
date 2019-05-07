import unittest

from ..app.page_downloader import PageDownloader
from ..app.page_links_getter import PageLinksGetter
from ..app.wimoveis_element_transformer import WimoveisElementTransformer

class TestPageLinksGetter(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.wimoveis.com.br/apartamentos-venda-aguas-claras-df.html"
        self.page_downloader = PageDownloader(self.url)
        page = self.page_downloader.downloadPage()
        self.pages_links_getter = PageLinksGetter(page, {"class": "aviso"})
        self.elements = self.pages_links_getter.get_elements()
        self.wimoveis = WimoveisElementTransformer(self.elements)

    def test_get_elements(self):
        transformed_elements = self.wimoveis.Transform()
        self.assertIsNotNone(transformed_elements, "Elements transformed should not be none")

if __name__ == '__main__':
    unittest.main(exit=False)
