from queue import Queue
from threading import Lock
from time import time
import pandas as pd

from download_worker import DownloadWorker
from page_links_getter import GetAllPageLinks
from price_per_square_meter_analyzer import PricePerSquareMeterAnalyzer

apartments = []

def main():
    ts = time()
    queue = Queue()
    mainUrl = "https://www.wimoveis.com.br/apartamentos-venda-aguas-claras-df-ordem-publicado-maior.html"
    #mainUrl = "https://www.wimoveis.com.br/apartamentos-venda-brasilia-df.html"

    threadLock = Lock()
    for x in range(8):
        worker = DownloadWorker(queue, threadLock, apartments)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    for url in GetAllPageLinks(mainUrl):
        print('Queueing {}'.format(url))
        queue.put(url)
    queue.join()
    print('Finished')
    print('Took %s seconds', time() - ts)

    analyzer1 = PricePerSquareMeterAnalyzer(apartments)
    ap2 = analyzer1.Analyze()

    df = pd.DataFrame(ap2)
    writer = pd.ExcelWriter('output-aguas-claras.xlsx')
    df.to_excel(writer, 'apartments')
    writer.save()
    print("Results analyzed and saved")

if __name__ == '__main__':
    main()