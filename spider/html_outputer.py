class HtmlOutputer(object):

    def __init__(self):
        self.dataList = []

    # ?????????? dataList
    def collect_data(self, data):
        if data is not None:
            self.dataList.append(data)


    # ? DataList ???????? output.html
    def outputer_html(self):
        out = open('output.html', 'w', encoding='utf-8')

        out.write("<html>")
        out.write("<meta charset='utf-8'>")
        out.write("<body>")
        out.write("<table border='1'>")

        for data in self.dataList:
            out.write("<tr>")

            out.write("<td>%s</td>" % data['url'])
            out.write("<td>%s</td>" % data['title'])
            out.write("<td>%s</td>" % data['summary'])

            out.write("</tr>")

        out.write("</table>")
        out.write("</body>")
        out.write("</html>")

        out.close()
