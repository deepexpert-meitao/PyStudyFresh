import re  
import urllib  
import urllib2  
import cookielib  
  
data = {"searchType":"common","searchedDomainName":"ass","suffix":".com"}  
post_data = urllib.urlencode(data)  
cj = cookielib.CookieJar  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0"}  
req = urllib2.Request("http://www.zgsj.com/domain_reg",post_data,headers)  
content = urllib2.urlopen(req)  
print content.read()
__author__ = 'Administrator'
s1 = set(open('C:\\Users\\Administrator\\Desktop\\a.txt','r').readlines())
s2 = set(open('C:\\Users\\Administrator\\Desktop\\b.txt','r').readlines())
print s1-s2
print s2-s1
<span style="font-size:14px;">


class First_Spider:
    def getpage(self,name,suffix='.com'):
        data = {"d_name":"","dtype":"common","drand":".1416113688132"}
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

    def addname(self):
        for n1 in range(97,123):
            self.getpage(chr(n1))
            for n2 in range(97,123):
                self.getpage(chr(n1)+chr(n2))
                for n3 in range(97,123):
                    print "I am texting domain name starting with",chr(n1),chr(n2),chr(n3)
                    self.getpage(chr(n1)+chr(n2)+chr(n3))
                    for n4 in range(97,123):
                        self.getpage(chr(n1)+chr(n2)+chr(n3)+chr(n4))
                        for n5 in range(97,123):
                            self.getpage(chr(n1)+chr(n2)+chr(n3)+chr(n4)+chr(n5))



myspider = First_Spider()
myspider.addname()</span>