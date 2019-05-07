from threading import Thread

from page_downloader import PageDownloader
from page_links_getter import PageLinksGetter
from wimoveis_element_transformer import WimoveisElementTransformer


class DownloadWorker(Thread):

    def __init__(self, queue, lock, apartments):
        Thread.__init__(self)
        self.queue = queue
        self.lock = lock
        self.apartments = apartments

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            url = self.queue.get()
            try:
                aps = DownloadAllInOnePage(url)
                with self.lock:
                    self.apartments.extend(aps)
                    print("Total downloaded: " + str(len(self.apartments)))
            finally:
                self.queue.task_done()


def DownloadAllInOnePage(url):
    print('Downloading from ' + url)
    page_downloader = PageDownloader(url)
    page = page_downloader.downloadPage()
    page_links_getter = PageLinksGetter(page, {"class": "aviso"})
    witransformer = WimoveisElementTransformer(page_links_getter.get_elements())
    apartments = witransformer.Transform()
    return apartments


