__author__ = '我叫MT'
# encoding: utf-8
import cookielib
import urllib2

cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

headers = {'User-agent":"Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0'}

request = urllib2.Request("http://store.apple.com/hk-zh/buy-iphone/iphone6/", post_data, headers)
operate = opener.open(request)

print operate.read()