#/usr/local/bin/env python
#coding:utf-8

import urllib
import urllib2
import cookielib
import re
import bs4

class SGS:
    def __init__(self):
        self.loginUrl = 'http://www.sgs.gov.cn/lz/etpsInfo.do?method=doSearch'
        self.gradeUrl = 'http://www.sgs.gov.cn/lz/etpsInfo.do?method=viewDetail'
        self.cookies = cookielib.CookieJar()  
        self.postdata = urllib.urlencode({
            'searchType':'1',
            'keyWords':'上海来伊份电子商务有限公司'
          })
        self.headers = {
            'Host':'www.sgs.gov.cn',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection' : 'Keep-Alive',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
        }
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        request = urllib2.Request(
            url = self.loginUrl,
            data = self.postdata,
            headers = self.headers)
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
        postid = self.getEspsid()
        newpostdata = urllib.urlencode({'espId':postid})
        newheaders = {
            'Host':'www.sgs.gov.cn',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection' : 'Keep-Alive',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Referer':'http://www.sgs.gov.cn/lz/etpsInfo.do?method=doSearch'
        }    
        print newheaders
        newRequest = urllib2.Request(url=self.gradeUrl,data=newpostdata,headers=newheaders)
        #    url = self.gradeUrl,
        #   data = newpostdata)
        result = self.opener.open(newRequest)
        contents = result.read()
        print contents
        

               
sgs = SGS()
sgs.getResult()
