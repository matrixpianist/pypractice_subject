import requests
from lxml import etree
q = []
class Ganhan(object):
    def __init__(self):
        self.base_url = "http://www.gxny.gov.cn/xwdt/zhyyjgl/201812/t20181226_539321.html"
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Mobile Safari/537.36'
        }
    def request(self,url):
        respose = requests.get(url,headers = self.header)
        data = respose.content.decode()
        return data
    def pare_data(self,data):
        x_data = etree.HTML(data)
        a = x_data.xpath('//tr')
        print(len(a))

        for i in a:
            a = i.xpath('.//td/p/strong/span/text()')

            c = i.xpath('.//td/p/span/text()')

            q.append(c)
            print(q)
    def save(self,data):
        pass
    def run(self):
        url = self.base_url
        data = self.request(url)
        data = self.pare_data(data)


Ganhan().run()
