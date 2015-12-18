### 基本流程

```
爬虫调度端 -> URL管理器 -> 网页下载器 -> 网页解析器  -> 有价值数据
              ↑                          |
              ↑--------------------------|
```


### URL管理器  
管理待抓取URL集合和已抓取集合

### 网页下载器
将网络上的HTML文件下载下来

#### 第一种方式
```python
import urllib2

# 直接请求
response = urllib2.urlopen('http://www.baidu.com')

# 获取状态码，如果是 200 表示获取成功
print response.getcode()

# 读取内容
cont = response.read()
```

#### 第二种方式
```python
import urllib2

# 创建 Request 对象
request = urllib2.Request(url)

# 添加数据
request.add_data('a','1')

# 添加 Http 的 Header
request.add_header('User-Agent','Mozilla/5.0')

# 发送请求获取结果
response = urllib2.urlopen(request)

```

#### 第三种方式
```python
import urllib2, cookielib

# 创建 Cookie 容器
cj = cookielib.CookieJar()

# 创建 1 个 opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# 给 urllib2 安装 opener
urllib2.install_opener(opener)

# 使用带有 cookie 的 urllib2 访问网页
response = urllib2.urlopen('http://www.baidu.com')

```

### 网页解析器
* 正则表达式
* html.parser
* Beautiful Soup
* lxml

第一种是模糊匹配，后三者会解析成DOM树，再进行一些操作。  

#### Beautiful Soup 文档
`http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/`  
文档中显示`例子在Python2.7和Python3.2中的执行结果相同`，所以大家不用担心版本问题  
使用命令安装 `pip install beautifusoup4`  

#### 简单使用
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(
	html_doc,             # HTML 文档字符
	'html.parse'          # HTML 解析器
	from_encoding='utf8'  # HTML 文档的编码
)

# 查找所有标签为 a 的节点
soup.find_all('a')

# 查找所有标签为a，链接符合 /view/123.html 形式的节点
soup.find_all('a',href='/view/123.html')
soup.find_all('a',href=re.compile(r'/view/\d+\.html'))

# 查找所有标签为 div， class 为 abc ，文字为 Python 的节点
soup.find_all('div',class_='abc',string='Python')

# 假如得到节点 <a href="/categroy">Python</a>

# 获取查到节点的标签名称
node.name

# 获取查到节点的 href 属性
node['href']

# 获取查到链接的文字
node.get_text()
```

```python
# 官网上的 demo
from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,"html.parser")

print(soup.find_all('a'))

```





