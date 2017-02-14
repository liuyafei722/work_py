from taobao import url_manager
from taobao import html_downloader
from taobao import html_parser
from taobao import html_outputer
class TaobaoMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlFownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def crew(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url()
            try:
                new_url = self.urls.get_new_url()#从URL管理器中获取一条URL
                print('craw ', count, ':', new_url)
                html_cont = self.downloader.download(new_url)#返回的是下载下来的dom树
                new_urls, new_data = self.parser.paser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 100
                    break
                count = count + 1

            except:
                print("craw failed")

if __name__ == "__main__"
    root_url = ""
    obj_crew = TaobaoMain()
    obj_crew.crew(root_url)
