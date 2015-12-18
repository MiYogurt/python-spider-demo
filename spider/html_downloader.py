import urllib.request

class HtmlDownloader(object):
        
    def download(self, url):
        if url is None:
            return None

        req = urllib.request.Request(url)

        response = urllib.request.urlopen(req)

        data = response.read()

        return data
