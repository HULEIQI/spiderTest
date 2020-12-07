""" 爬虫练习，获取豆瓣 top250 电影名"""

import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/13.1.2 Safari/605.1.15"
}
url = "https://movie.douban.com/top250?start="
response = requests.get(url=url, headers=headers).text
data = BeautifulSoup(response, "html.parser")

""" 获取所有标签"""
# top250_titles = data.find_all("img")
# for top250_title in top250_titles:
#     print(top250_title)


# 定义一个函数
# def name_is_exist(tag):
#     return tag.has_attr("id")
# title_list = data.find_all(name_is_exist)
# print(title_list)

# 2 id=?
# print(data.find_all(class_="item"))

# 3 text参数
# t_list = data.find_all(text=re.compile(r"\d"))

# 4 limit
# t_list = data.find_all("a", limit=3)
# for item in t_list:
#     print(item)

"""css选择器"""
# print(data.select('title'))  # 通过标签查找

# t_list = data.select('.other')  # 通过类名来查找

# t_list = data.select('#other')  # 按照 id 查找

# t_list = data.select("div[class='item']")  # 通过属性来查找

# t_list = data.select("meta > title")  # 通过子标签来查找

# t_list = data.select(".other")  # 获取标签内容
# print(t_list[0].get_text())
# for item in t_list:
#     print(item)


"""正则表达式：字符串是否符合一定标准"""
# pat = re.compile('AA')  # 此处的AA是正则表达式，用来去验证其他的字符串
# m = pat.search('ABC')  # search 字符串被校验的内容
# m = pat.match('AABBCC')
# m = re.search('AA', 'AadsadaAAdasdsa')  # 前一个字符串是规则，后一个是被校验对象
# m = pat.search('AABBCCAABBFFAA')
# print(m)
# print(re.findall('a', "aaaSadafdsfsa"))
# print(re.findall('[A-Z]+', "aaaSaDFFFafdsFsa"))
# print(re.sub('a', 'A', 'AAAaaaaa')) # 找到a用A替代，在第三个字符串中查找







