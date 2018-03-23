#!/usr/bin/env python
import urllib
import urllib2
import requests

headers={
'Host': '110.65.10.184',
'Cache-Control': 'max-age=0',
'Origin': 'http://110.65.10.184',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://110.65.10.184/xf_xsqxxxk.aspx?xh=201730631162&xm=%C0%EE%B1%F2&gnmkdm=N121103',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'ASP.NET_SessionId=hvuoatfsjcauwvf43atvwqyq',
'Connection': 'close'
}

data = open("base", "r").read()

payload={
	'xh': '201730631162',
	'xm': '%C0%EE%B1%F2', 
	'gnmkdm': 'N121103',
	'__EVENTTARGET': "",
	"__EVENTARGUMENT": "", 
	"__VIEWSTATE": data,
	"ddl_kcxz": "",
	"ddl_ywyl": "",
	"ddl_kcgs": "",
	"ddl_xqbs": "2",
	"ddl_sksj": "",
	"TextBox1": "",
	"kcmcGrid%3A_ctl8%3Axk": "on",
	"dpkcmcGrid%3AtxtChoosePage": 1,
	"dpkcmcGrid%3AtxtPageSize": 15,
	"Button1": "++%CC%E1%BD%BB++"
}

url = "http://www.scut.edu.cn/jw2005/xf_xsqxxxk.aspx"

d = requests.post(url,data=payload,headers=headers)
print d