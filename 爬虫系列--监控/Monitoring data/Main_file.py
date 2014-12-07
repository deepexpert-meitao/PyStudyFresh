__author__ = '我叫MT'
#coding:utf-8

import requests
import time
import MySQLdb
import re


def write_to_mysql():
    try:
        cxn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='python')     #与数据库建立连接

    except:
        print "Could not connect to MySQL server."
        exit(0)

    cur = cxn.cursor()
    cur.execute("CREATE TABLE dollar(Local_time VARCHAR(20), USDCNH VARCHAR(8),DINIW  VARCHAR(8))")	    #记录时间、汇率、美元指数三个参数
    cur.execute("create table oil(Local_time VARCHAR(20), CONC VARCHAR(20))")		    #记录时间、原油指数两个参数

    while 1:
        value1 = []
        value2 = []
        result(value1, value2)  #获取网页抓取的数据
        cur.execute("INSERT INTO dollar VALUES(%s, %s ,%s)", value1)
        cur.execute("INSERT INTO oil VALUES(%s, %s)", value2)
        cxn.commit()
        time.sleep(60*60)
    cxn.close()


def result(value1, value2):
    url1 = 'http://quote.eastmoney.com/gjqh/CONC.html'
    url2 = 'http://finance.sina.com.cn/money/forex/hq/DINIW.shtml?qq-pf-to=pcqq.c2c'

    html1 = requests.get(url1)
    html2 = requests.get(url2)

    ISOTIMEFORMAT = '%Y-%m-%d %X'
    value1.append(time.strftime(ISOTIMEFORMAT, time.localtime()))
    value2.append(time.strftime(ISOTIMEFORMAT, time.localtime()))

    USDCNY = re.compile('var hq_str_USDCNY=".*?,(.*?),.*?";').findall(html1.text)
    DINIW = re.compile('".*?,(.*?),.*?";').findall(html2.text)
    CONC = re.compile('extendedFutures:\["0.00,0|0.00,0",".*?,(.*?),.*?"]').findall(html3.text)

    value1.append(USDCNY[0].encode('utf-8'))
    value1.append(DINIW[0].encode('utf-8'))
    value2.append(CONC[1].encode('utf-8'))
    print value1, value2

write_to_mysql()