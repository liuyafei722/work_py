from baike import html_downloader
from baike import html_outputer
from baike import html_parser
from baike import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw ', count, ':', new_url)
                #print(new_url)
                html_cont = self.downloader.download(new_url)
                #print(html_cont)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                #print(new_data)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 110:
                     break
                count = count + 1

            except:
                print("craw failed")
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/2975166.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)