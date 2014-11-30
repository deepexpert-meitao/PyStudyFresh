__author__ = '我叫MT'
#coding:utf-8
import os, sys, string
import requests
import MySQLdb
import re
import urllib
import urllib2
import cookielib

conn = MySQLdb.connect(host='localhost', user='root', passwd="root", db='ttt')

cursor = conn.cursor()
sql = "create table if not exists test(name varchar(128) primary key, suffix varchar(128))"
cursor.execute(sql)


class First_Spider:
    def getpage(self, name, suffix='.com'):
        data = {"d_name":"","dtype":"common"}
        data["d_name"] = name+suffix
        post_data = urllib.urlencode(data)
        cj = cookielib.CookieJar
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0"}
        req = urllib2.Request("http://www.zgsj.com/domain_reg/domaintrans.asp",post_data,headers)
        content = urllib2.urlopen(req)
        c=content.read()
        pattern = re.compile('color:green;')
        p = pattern.findall(c)
        if p:
            print name
            sql = "insert into test(name, suffix) values('%s', '%s')" % (name,suffix)
            try:
                cursor.execute(sql)
            except Exception, e:
                print e

    def addname(self):
        for n1 in range(97, 123):
            self.getpage(chr(n1))
            for n2 in range(97, 123):
                self.getpage(chr(n1)+chr(n2))
                for n3 in range(97, 123):
                    print "I am testing domain name starting with", chr(n1), chr(n2), chr(n3)
                    self.getpage(chr(n1)+chr(n2)+chr(n3))
                    for n4 in range(97, 123):
                        self.getpage(chr(n1)+chr(n2)+chr(n3)+chr(n4))
                        for n5 in range(97, 123):
                            self.getpage(chr(n1)+chr(n2)+chr(n3)+chr(n4)+chr(n5))

myspider = First_Spider()
myspider.addname()

cursor.close()
conn.close()