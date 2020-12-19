import scrapy
import xlwt

from ITcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['www.itcast.cn']
    start_urls = ['http://www.itcast.cn/']

    # def parse(self, callback=response):
    def parse(self, response):
        # 把数据封装到一个 ItcastItem 对象
        item = ItcastItem()
        node_list = response.xpath("/html/body/div[2]/div[12]/div/div[3]/div[1]/div[2]/ul[*]/li[*]")

        """爬取 http://www.itcast.cn/ 老师信息的xpath设置"""
        # response.xpath("/html/body/div[2]/div[12]/div/div[3]/div[1]/div[2]/ul[1]/li[1]/div[2]")
        # "/html/body/div[2]/div[12]/div/div[3]/div[1]/div[2]/ul[1]/li[1]/div[2]"
        # "/html/body/div[2]/div[12]/div/div[3]/div[1]/div[2]/ul[1]/li[1]/div[3]"
        # "/html/body/div[2]/div[12]/div/div[3]/div[1]/div[2]/ul[1]/li[1]"
        # "/html/body/div[2]/div[12]/div/div[3]/div[1]/div[2]/ul[1]/li[2]"

        """不存在翻页 ul[1]"""
        # node_list = response.xpath("/html/body/div[2]/div[12]/div/div[3]/div[1]/div[2]/ul[1]/li[*]")
        # for node in node_list:
        #     name = node.xpath("./div[*]/h2/text()").extract()[0]
        """翻页 ul[*]"""
        # node_list = response.xpath("/html/body/div[2]/div[12]/div/div[3]/div[1]/div[2]/ul[*]/li[*]")

        # workbook = xlwt.Workbook(encoding="utf-8")
        # # 新建电子表格 sheet1
        # worksheet = workbook.add_sheet("sheet1")
        # # 在 sheet1(0, 0)处写入标题内容"名字"
        # worksheet.write(0, 0, "名字")
        # # 换行写入标志
        # low_num = 1
        # for node in node_list:
        #     # 获取老师的名字
        #     name = node.xpath("./div[*]/h2/text()").extract()[0]
        #     # 将获取到的老师名字写入到电子表格中
        #     worksheet.write(low_num, 0, name)
        #     # 每写入一个数据，换行写入标志加一
        #     low_num += 1

        # workbook.save("name.xls")  # 在当前目录下，保存为 name.xls

        """2、写入管道"""
        for node in node_list:
            # 获取老师的名字
            name = node.xpath("./div[*]/h2/text()").extract()
            # 获取老师的入职时间
            employment_date = node.xpath("./div[3]/h3/text()").extract()
            item["name"] = name[0]
            item["employment_date"] = employment_date[0]
            yield item
