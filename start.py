#开发人员：林泽鑫
#开发实践：2019/8/4 0:57
#文件名称：start.py
#开发工具: PyCharm

from scrapy import cmdline

cmdline.execute("scrapy crawl httpbin".split())