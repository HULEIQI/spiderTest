# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class ItcastPipeline:
    """管道可以设置多个，在setting"""
    def open_spider(self, spider):
        # open("itcast_pineline.json", "w") 和 open("itcast_pineline.json", "wb")
        self.file = open("itcast_pineline.json", "wb")

    def process_item(self, item, spider):
        # dump 和 dumps 的区别
        # unicode, ascii, decode, encoding
        # \u5468\u8001\u5e08 使用unicode码，需要设置 ensure_ascii=False
        content = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False)+"\n"
        self.file.write(content.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.file.close()
