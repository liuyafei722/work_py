class UrlManager(object):
    def __init__(self):
        self.new_urls = set()#用集合来存储要爬取的url
        self.old_urls = set()

    def add_new_url(self, url):#将新的url添加到
        if url is None:
            print("manager中是空的")
            return

        if url not in self.new_urls and url not in self.old_urls:
            print("manager中不是是空的")
            self.new_urls.add(url)
            print(self.new_urls)

    def has_new_url(self):#在当前URL管理器中是否还有未被抓取的URL
        return len(self.new_urls) != 0

    def get_new_url(self):#在当前未被抓去的URL中返回一个URL病添加到old_urls
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url



    def add_new_urls(self, urls):#一次性添加多条url
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)