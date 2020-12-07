import requests
import re
from bs4 import BeautifulSoup
import xlwt
import sqlite3

# baseURL = "https://movie.douban.com/top250?start="  # url 不要放这里
# 规则
# 查找影片链接
findLink = re.compile(r'href="(.*?)">')
# 查找影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符包含在字符中
# 查找影片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 查找影片评分
findRatingNum = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 查找影片评分人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 查找影片描述
findDescription = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取页面
def get_data(url):
    """提取 电影名、链接、介绍的信息并返回data_list列表
        BeautifulSoup 的使用
    """
    data_list = []  # 保存所有电影信息
    for i in range(0, 10):  # 调用获取页面信息的函数 10次
        new_url = url + str(i*25)
        html = ask_url(new_url)

        # 2. 逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='item'):
            # print(item)  # 测试查看电影的全部信息
            data = []  # 保存电影的所有信息：链接、图片、title...
            item = str(item)

            # 查看item格式，测试用，方便信息查看
            # print(item)
            # break

            # 保存影片名、链接、图片...等信息到data_list
            link = re.findall(findLink, item)[0]
            data.append(link)
            picture = re.findall(findImgSrc, item)[0]
            data.append(picture)
            name = re.findall(findTitle, item)[0]
            data.append(name)
            rate = re.findall(findRatingNum, item)[0]
            data.append(rate)
            judge = re.findall(findJudge, item)[0]
            data.append(judge)
            if re.findall(findInq, item):
                inq = re.findall(findInq, item)[0]
            else:
                inq = ''
            data.append(inq)
            description = re.findall(findDescription, item)[0]
            description = re.sub(r'<br(\s+)?/>(\s)?', ' ', description)
            # for items in data:
            #     print('%s = %s' % (type(items), items))
            # break
            data.append(description)
            data_list.append(data)
            # print(data)
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
            # judge = re.findall(findJudge, item)
            # print(judge)

            # 找到概况
            # inq = re.findall(findInq, item)
            # print(inq)

            # 获取影片描述
            # description = re.findall(findDescription, item)
            # print(description)
        # break
    return data_list


def ask_url(url):
    """爬取top500 html 内容并返回
        requests 的使用
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "Version/13.1.2 Safari/605.1.15"
    }
    html = requests.get(url=url, headers=headers).text
    return html


def save_data(path, content_inf):
    """保存豆瓣Top500抓取的数据到 excel"""
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    count = 0
    for i_content_inf in content_inf:
        # print(len(i_content_inf))
        # break
        for i in range(0, len(i_content_inf)):
            # print('%d %f' % (count, i), end='\t')
            worksheet.write(count, i, i_content_inf[i])
        count += 1
    workbook.save(path)


def save_database(dataList, dbpath):
    db_init(dbpath)
    for data in dataList:
        for index in range(len(data)):
            if index == 3 or index == 4:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movieDisplay (info_link,pic_link,cname,score,rated,instruction,info)
             values(%s)
        ''' % ",".join(data)

        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    # conn = sqlite3.connect("test.db")  # 创建 database
    # print("创建数据库成功！")
    # conn_start = conn.cursor()  # 定位游标
    # # link、picture、name、rate、judge、inq、description
    # # sql = '''
    # #     create table dou_ban_Top500(
    # #         id int Primary Key not null,
    # #         link char(250) null,
    # #         picture char(250) null,
    # #         name char(250) null,
    # #         rate char(250) null,
    # #         judge char(250) null,
    # #         inq char(250) null,
    # #         description char(250) null);
    # # '''
    # # sql2 = '''
    # #     insert into dou_ban_Top500 (id,link,picture,name,rate,judge,inq,description)
    # #      values (1,"link","picture","name","rate","judge","inq","description")
    # # '''
    # sql3 = '''
    #     insert into dou_ban_Top500(id,link,picture,name,rate,judge,inq,description)
    #      values (?,?????)
    # '''
    # conn_start.execute(sql3)  # 执行 sql 语句
    # print("创建表成功！")
    # conn.commit()  # 提交数据库
    # conn.close()  # 关闭数据库链接


def db_init(dbpath):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    sql = '''
        create table movieDisplay(
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            score numeric,
            rated numeric,
            instruction text,
            info text
        )
    '''
    sql1 = 'drop table movieDisplay'
    cursor.execute(sql)
    # cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    baseURL = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    dataList = get_data(baseURL)
    # save_path = "douBan_movie_Top500.xls"
    # 3.保存数据
    # save_data(save_path, dataList)
    dbpath = "movieDB"
    save_database(dataList, dbpath)
    print("爬取成功")
