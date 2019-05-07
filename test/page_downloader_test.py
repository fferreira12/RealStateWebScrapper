import unittest

from ..app.page_downloader import PageDownloader


class TestPageDownloader(unittest.TestCase):

    def setUp(self):
        self.url = "http://www.wimoveis.com.br/apartamentos-venda-aguas-claras-df.html"
        self.page_downloader = PageDownloader(self.url)

    def test_get_url(self):
        page = self.page_downloader.downloadPage()
        self.assertIsNot("", page, "Page retrieved should not be none")


if __name__ == '__main__':
    unittest.main(exit=False)
