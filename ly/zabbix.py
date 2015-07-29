
#coding:utf-8
##


import urllib
import urllib2
import cookielib
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class searchInfo:
    def __init__(self):
        #初始化访问信息
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
        self.initUrl = 'http://1.2.4.1/index.php'
        self.searchUrl = 'http://1.2.4.1/report2.php'
        self.cookies = cookielib.CookieJar()
        self.postdata01 = urllib.urlencode({
            'autologin':'1',
            'enter':'Sign in',
            'name':'admin',
            'password':'111111',
            'request':''
            })
        self.postdata02 = urllib.urlencode({
            'config':'0',
            'filter_groupid':'15',                       
            'filter_hostid':'0',
            'filter_timesince':'20150610000000',
            'filter_timesince_day':'10',
            'filter_timesince_hour':'00',
            'filter_timesince_minute':'00',
            'filter_timesince_month':'06',
            'filter_timesince_year':'2015',
            'filter_timetill':'20150615000000',
            'filter_timetill_day':'15',
            'filter_timetill_hour':'00',
            'filter_timetill_minute':'00',
            'filter_timetill_month':'06',
            'filter_timetill_year':'2015',
            'form':'1',
            'form_refresh':'1',
            'sid':'181aa0d0297c68c8'
            })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    
    def getPage(self):
        #获取搜索结果页面
        request01 = urllib2.Request(
            url = self.initUrl,
            data = self.postdata01,
            headers = self.headers)
        request02 = urllib2.Request(
            url = self.searchUrl,
            data= self.postdata02,
            headers = self.headers)

        result = self.opener.open(request01)
        result = self.opener.open(request02)
        contents = result.read()
        unicodePage = contents.decode("utf-8")
        return unicodePage

    def save_data(self):
        page = self.getPage()
        pattern = re.findall('<tr.*?class="(?:even_row|odd_row)".*?>.*?<td>(.*?)<\/td>.*?<td>.*?<a.*?href="events.php.*?>(.*?)<\/a>.*?<\/td>.*?<td>.*?<span.*?class="on">(.*?)<\/span>.*?<\/td>.*?<td>.*?<span.*?class="off">(.*?)<\/span>',page,re.S)
        file = open('/opt/test.log','w+')
        for item in pattern:
            line = []
            line = [item[0],item[1],item[2],item[3]]
            file.writelines('\t'.join(line)+'\n')
        file.close()


zabbix = searchInfo()
zabbix.save_data()
