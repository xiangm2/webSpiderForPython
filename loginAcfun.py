# -*- coding: cp936 -*-
import requests
import time
import datetime
import traceback
import json
import urllib

    
def loginAcFun(username,password):
    'login acfun'
    loginurl = 'http://www.acfun.cn/login.aspx'
    headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Content-Length':'40',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Host':'www.acfun.cn',
    'Origin':'http://www.acfun.cn',
    'Referer':'http://www.acfun.cn/login/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'}
    data = {'username':username,'password':password}
    s = requests.Session()
    try:
        r = s.post(url = loginurl,data=data,headers=headers)
        if r.json()['success'] == True:
            print '{} Login success at {}'.format(r.json()['username'],time.ctime())
            #print r.cookies
        else:
            print r.json()['result']
    except Exception ,diag:
        print str(diag)
    #访问其他页面,开始进行模拟签到
    signurl = 'http://www.acfun.cn/webapi/record/actions/signin'
    postdata = {'channel':0,'date':int(time.time())*1000}
    m = s.post(signurl,data = postdata)
    print m.url
    #print m.status_code
    print m.json()
    print m.json()['message']
if __name__ == '__main__':
    loginAcFun(username,password)




