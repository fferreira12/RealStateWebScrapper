class PricePerSquareMeterAnalyzer():

    def __init__(self, estates):
        self.estates = estates

    def Analyze(self):
        for ap in self.estates:
            if ap['price'] == -1 or ap['area'] == -1 or ap['area'] == 0:
                continue
            ap['price_per_square_meter'] = ap['price'] / ap['area']
        return self.estates