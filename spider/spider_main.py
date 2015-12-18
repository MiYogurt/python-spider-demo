from spider import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):
    """爬虫入口"""
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
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                print(new_data, "/n")
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                # print('craw success {0} : {1}'.format(count, new_url))
                count = count + 1

                if count > 10:
                    break

            except Exception as e:
                print("Has Some Error: ", e)
          
        self.outputer.outputer_html()



if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/592799.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
