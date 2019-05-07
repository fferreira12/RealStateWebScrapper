from bs4 import BeautifulSoup

from element_transformer import ElementTransformer


class WimoveisElementTransformer(ElementTransformer):

    def __init__(self, elements):
        self.elements = elements

    def setElements(self, elements):
        self.elements = elements

    def Transform(self):
        newElements = []
        for element in self.elements:
            el = {}
            el['id'] = element["id"].split('-')[1]
            el['adress'] = " ".join(element.find_all('span', attrs={"class": "aviso-data-location dl-aviso-link"})[0].contents[0].split())
            el['city'] = str(element.find_all('span', attrs={"class": "aviso-data-location dl-aviso-link"})[0].contents[1].contents[0])
            el['title'] = element.find_all('a', attrs={"class": "dl-aviso-a"})[0]['title']
            try:
                el['price'] = int(element.find(attrs={"class":"avisoPrecio"})["value"].replace(".", "").split(" ")[1])
            except:
                el['price'] = -1
            try:
                el['area'] = int(element.find_all("li", attrs={"class":"aviso-data-features-value"})[0].contents[0].strip().split(' ')[0])
            except:
                el['area'] = -1
            try:
                el['rooms'] = int(element.find_all("li", attrs={"class":"aviso-data-features-value"})[1].contents[0].strip())
            except:
                el['rooms'] = -1
            try:
                el['bathrooms'] = int(element.find_all("li", attrs={"class":"aviso-data-features-value"})[2].contents[0].strip())
            except:
                el['bathrooms'] = -1
            newElements.append(el)

        return newElements