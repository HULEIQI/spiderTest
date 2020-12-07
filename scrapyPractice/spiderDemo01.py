"""
# 查找影片描述内容时候有问题！！！
"""
import requests
import re
from bs4 import BeautifulSoup

baseURL = "https://movie.douban.com/top250?start="
# 规则
# 查找影片链接
findLink = re.compile(r'href="(.*)">')
# 查找影片图片
findImgSrc = re.compile(r'<img.*src="(.*)"', re.S)  # re.S让换行符包含在字符中
# 查找影片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 查找影片评分
findRatingNum = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 查找影片评分人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 查找影片描述
findDescription = re.compile(r'<p class="">(.*)</p>', re.S)


# 爬取页面
def get_data(url):
    for i in range(0, 1):  # 调用获取页面信息的函数 10次
        url = url + str(i * 25)
        html = ask_url(url)

        # 2. 逐一解析数据
        data_lists = ask_url(baseURL)
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='item'):
            # print(item)  # 测试查看电影的全部信息
            data = []  # 保存一步电影的所有信息
            item = str(item)

            # 查看格式
            # print(item)
            # break

            # 查找电影详情链接
            # link = re.findall(findLink, item)[0]  # re库通过正则表达式查找指定的字符串
            # print(link)

            # 查找电影图片
            # picture = re.findall(findImgSrc, item)[0]
            # print(picture)

            # 查找电影名
            # name = re.findall(findTitle, item)[0]
            # print(name)

            # 查找评分
            # rate = re.findall(findRatingNum, item)[0]
            # print(rate)

            # 查找影片评分人数
            # judge = re.findall(findJudge, item)[0]
            # print(judge)

            # 找到概况
            # inq = re.findall(findInq, item)[0]
            # print(inq)

            # 获取影片描述
            description = re.findall(findDescription, item)
            print(description[0])



def ask_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "Version/13.1.2 Safari/605.1.15"
    }
    html = requests.get(url=url, headers=headers).text
    return html


if __name__ == '__main__':
    get_data(baseURL)
    # ask_url("https://movie.douban.com/top250?start=")
