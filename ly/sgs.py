
#coding:utf-8

import urllib
import urllib2
import cookielib
import re
#import sys 
#reload(sys) 
#sys.setdefaultencoding('utf-8')

class searchInfo:
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
        self.initUrl = 'http://www.36yc.com'
        self.searchUrl = 'http://www.36yc.com/search'
        #self.viewUrl = 'http://ww.36yc.com/%s +'+ % str(viewDetailUrl)
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'area':'shanghai',
            'key':'上海来伊份电子商务有限公司',
            'search':'查企业',
            't':'ent_name'
            })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        request = urllib2.Request(
            url = self.searchUrl,
            data = self.postdata,
            headers = self.headers)
        result = self.opener.open(request)
        contents = result.read()
        #return contents.encode('utf8')
        unicodePage = contents.decode("utf-8")
        return unicodePage


    def getlink(self):
        page = self.getPage()
       # print page
        pattern = re.findall('<tr>.*?<tr>.*?<td>(.*?)<\/td>.*?<td>.*?<\/td><td>.*?<\/td><td><a href="(.*?)".*?target=".*?',page,re.S)
        items = []
        #print pattern
        #for item in pattern:
        #    items.append(item[0].encode('utf-8'))
        #print items[0]
        for item in pattern:
            items.append(item[1])
        return items[0]
        
        
        #print items
        #companyName = items[0]
        #companyLink = items.groups(2)
        #print companyName.encode
        #print companyLink.encode

    def getViewPage(self):
        viewLink = self.getlink()
        viewUrl = self.initUrl + viewLink
        viewRequest = urllib2.Request(url = viewUrl,headers = self.headers)
        viewResult = self.opener.open(viewRequest)
        viewContents = viewResult.read()
        viewUnicodePage = viewContents.decode("utf-8")
        return viewUnicodePage

    def getResult(self):
        viewPage = self.getViewPage()
        fucker = re.findall('<td.*?class=".*?width=.*?><strong>(.*?)<\/strong><\/td>',viewPage,re.S)
        print fucker[2].encode('utf-8')
        #result = []
        #for item in fucker:
        #    result.append(item[0].encode('utf-8'))
        #print result[0]

               
sgs = searchInfo()
sgs.getResult()
