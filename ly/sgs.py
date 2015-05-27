#/usr/local/bin/env python
#coding:utf-8

import urllib
import urllib2
import cookielib
import re


class SGS:
    def __init__(self):
        self.loginUrl = 'http://www.sgs.gov.cn/lz/etpsInfo.do?method=doSearch'
        self.gradeUrl = 'http://www.sgs.gov.cn/lz/etpsInfo.do?method=viewDetail'
        self.cookies = cookielib.CookieJar()  
        self.httpHandler = urllib2.HTTPHandler(debuglevel=1)
        self.postdata = urllib.urlencode({
            'searchType':'1',
            'keyWords':'上海来伊份电子商务有限公司'
          })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        request = urllib2.Request(
            url = self.loginUrl,
            data = self.postdata)
        result = self.opener.open(request)
        contents = result.read()
        return contents

    def getEspsid(self):
        page = self.getPage()
        items = re.findall(u'<a href=.*?viewDetail\(\'(\d+)\'\).*?>',page,re.S)
        if items:
            espsid = items[0]
            return espsid
            print type(espsid)
        else:
            print "Not Found"

    def getResult(self):
        postid = int(self.getEspsid())
        newpostdata = urllib.urlencode({'espId':postid})
        
        headers = {
            'Referer':'http://www.sgs.gov.cn/lz/etpsInfo.do?method=doSearch',
            'Cache-Control':'max-age=0'
        }    
        print headers
        newRequest = urllib2.Request(url=self.gradeUrl,data=newpostdata,headers=headers)
        #    url = self.gradeUrl,
        #   data = newpostdata)
        result = self.opener.open(newRequest)
        contents = result.read()
        print contents

        

               
sgs = SGS()
sgs.getResult()
