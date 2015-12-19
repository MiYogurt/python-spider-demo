import urllib.request

class HtmlDownloader(object):

    # 下载到 url 链接的 HTML 文档
    def download(self, url):
        if url is None:
            return None

        req = urllib.request.Request(url)

        response = urllib.request.urlopen(req)

        data = response.read()

        return data
