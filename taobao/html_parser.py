import re
import urllib.parse
from bs4 import BeautifulSoup


class HtmlParser(object):

    def paser(self, page_url, html_cont):
        if page_url is None:
            print("return")
            return
        print(html_cont)
        soup = BeautifulSoup(html_cont, 'html.parser',
                             from_encoding='utf-8')  # 建立一个beautifulsoup对象
        # print(soup)
        new_urls = self._get_new_urls(page_url, soup)
        print(new_urls)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find('a', href=re.compile(r"http://item\.taobao\.com/+"))
        print(links)
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
            print("this is new url", new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        title_node = soup.find('div', class_="tb-detail-hd").find("h1")
        res_data['title'] = title_node.get_text()
        #<div class="tm-rate-fulltxt">差评！差评！差评！发美国、到现在20天了、快递一直不更新、问了几次、现在干脆不回复我了、?都付款了、我想问问货哪去了！</div>
        comment_node = soup.find('div', class_="tm-rate-fulltxt")
        res_data['comment'] = comment_node.get_text()
        return res_data
