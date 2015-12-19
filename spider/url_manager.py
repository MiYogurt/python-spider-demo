class UrlManager(object):
    # 维护俩个Set,已抓取过的old_urls,和未抓取过的new_urls
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 将新的url添加到 new_urls 中
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls: # 判断 url 不在 old_urls 和 new_urls 里面才添加
            self.new_urls.add(url)

    # 将新的 urls[list] 添加到 new_urls 中
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)    

    # 得到一个从 new_urls 中出栈的 url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    # 判断 new_urls 里面时候还有 url
    def has_new_url(self):
        return len(self.new_urls) != 0   