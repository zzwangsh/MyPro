
#coding:utf-8

import urllib
import urllib2
import cookielib
import re

'''
Usage: 主要作用是从网站上获取企业法定代表人
'''

class searchInfo:
    def __init__(self):
        #初始化访问信息
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
        self.initUrl = 'http://www.36yc.com'
        self.searchUrl = 'http://www.36yc.com/search'
        self.cookies = cookielib.CookieJar()
        #此处指定post数据，需要注意下面字符有时候会变
        self.postdata = urllib.urlencode({
            'area':'shanghai',
            'key':'上海来伊份电子商务有限公司',
            'search':'查企业',
            't':'ent_name'
            })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    
    def getPage(self):
        #获取搜索结果页面
        request = urllib2.Request(
            url = self.searchUrl,
            data = self.postdata,
            headers = self.headers)
        result = self.opener.open(request)
        contents = result.read()
        unicodePage = contents.decode("utf-8")
        return unicodePage

    def getlink(self):
        #根据结果页面正则去除匹配的详细页面链接
        page = self.getPage()
        pattern = re.findall('<tr>.*?<tr>.*?<td>(.*?)<\/td>.*?<td>.*?<\/td><td>.*?<\/td><td><a href="(.*?)".*?target=".*?',page,re.S)
        items = []
        for item in pattern:
            items.append(item[1])
        return items[0]

    def getViewPage(self):
        #根据 getlink() 获取到的链接，request详细页面
        viewLink = self.getlink()
        viewUrl = self.initUrl + viewLink
        viewRequest = urllib2.Request(url = viewUrl,headers = self.headers)
        viewResult = self.opener.open(viewRequest)
        viewContents = viewResult.read()
        #因为取出来的是汉字，此处注意需要转码，不然后面会以ascii码形式显示
        viewUnicodePage = viewContents.decode("utf-8")
        return viewUnicodePage

    def getResult(self):
        #通过正则在详细页面当中获取公司法定代表人
        viewPage = self.getViewPage()
        fucker = re.findall('<td.*?class=".*?width=.*?><strong>(.*?)<\/strong><\/td>',viewPage,re.S)
        print fucker[2].encode('utf-8')
               
sgs = searchInfo()
sgs.getResult()
