import  urllib.request
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        print(response.getcode())
        if response.getcode() !=200:
            print(response.getcode())
            return None
        return response