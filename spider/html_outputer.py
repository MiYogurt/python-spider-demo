class HtmlOutputer(object):

    def __init__(self):
        self.dataList = []

    def collect_data(self, data):
        if data is not None:
            self.dataList.append(data)

    def outputer_html(self):
        out = open('output.html', 'w')

        out.write("<html>")
        out.write("<body>")
        out.write("<table>")

        for data in self.dataList:
            out.write("<tr>")

            out.write("<td>%s</td>" % data['url'])
            out.write("<td>%s</td>" % data['title'].encode('utf-8'))
            out.write("<td>%s</td>" % data['summary'].encode('utf-8'))

            out.write("</tr>")

        out.write("</table>")
        out.write("</body>")
        out.write("</html>")

        out.close()
