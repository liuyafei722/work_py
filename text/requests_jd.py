import requests
url = 'https://item.taobao.com/item.htm?spm=a219r.lm5179.14.8.1AvqSt&id=24229292833&ns=1&abbucket=2#detail'
resp = requests.get(url)
s = resp.text
print(s)
print(len(s))
with open('requests_jd.html', 'w', encoding = 'gbk') as f:
    f.write(s)


