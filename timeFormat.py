#!/user/bin/env python
# _*_ coding: utf-8 -*-
# @Time     :  9:24
# @Author   : kunlun_sun
# @Site     : 
# @File     : .py
# @Software : PyCharm Community Edition
import logging
import re

import time

import datetime

import pytz


def timeFormat(found_time):
    '''
    suport unix time(10p,13p) and  utc(Accurate to seconds and milliseconds) and yyyy-mm-dd hh:mm:ss
    eg:1502676456433 or 1502676456 or 2017-05-11T00:45:56Z or 2017-05-11T00:45:56.325Z or 2017-05-11 10:10:10
    '''
    if not found_time:
        return None
    found_time = str(found_time)
    if(re.match("\d{10,16}",found_time)):
        if(len(found_time)>=13):
            found_time = float(found_time)/1000
        else:
            found_time = float(found_time)
        ymd = time.localtime(found_time);
        return time.strftime("%Y-%m-%d %H:%M:%S",ymd)
    elif(re.search("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+[A-Z]",found_time)):
        matchArr = re.findall("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+[A-Z]",found_time)
        if(len(matchArr)>0):
            found_time = matchArr[0]
            utc_format = '%Y-%m-%dT%H:%M:%S.%f'+found_time[len(found_time)-1]
            local_tz = pytz.timezone("Asia/Shanghai")
            local_format = "%Y-%m-%d %H:%M:%S"
            utc_dt = datetime.datetime.strptime(found_time,utc_format)
            local_dt= utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
            local_s = local_dt.strftime(local_format)
            return local_s
    elif(re.search("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[A-Z]",found_time)):
        matchArr = re.findall("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[A-Z]",found_time)
        if(len(matchArr)>0):
            found_time = matchArr[0]
            utc_format = '%Y-%m-%dT%H:%M:%S'+found_time[len(found_time)-1]
            local_tz = pytz.timezone("Asia/Shanghai")
            local_format = "%Y-%m-%d %H:%M:%S"
            utc_dt = datetime.datetime.strptime(found_time,utc_format)
            local_dt= utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
            local_s = local_dt.strftime(local_format)
            return local_s
    else:
        ymd=re.findall('[0-9]+', found_time)
    if len(ymd)<3 or int(ymd[0])>2100 or int(ymd[0])<1800:
        return None
    if int(ymd[1])>12 or int(ymd[2])>31:
        return None
    if int(ymd[1]) not in (1,3,5,7,8,10,12) and int(ymd[2])>30:
            return None
    if int(ymd[1]) == 2:
        if int(ymd[2])>29:
            return None
        if int(ymd[2])==29:
            if int(ymd[0])%4!=0:
                return None
    if(len(ymd)>=6 and int(ymd[3])>=0 and int(ymd[3])<=24  and int(ymd[4])>=0 and int(ymd[4])<=60  and int(ymd[5])>=0 and int(ymd[5])<=60 ):
        return ymd[0]+"-"+ymd[1]+"-"+ymd[2]+" "+ymd[3]+":"+ymd[4]+":"+ymd[5]
    elif(len(ymd)==3):
        return  ymd[0]+ '-%02d'%int(ymd[1])  +'-%02d'%int(ymd[2])
    else:
        return None

xx = "2017年05月11 00:45:56Z";
yy = time.time();
print(timeFormat(xx))

# def utcform(utc_time):
#     utc_format = '%Y-%m-%dT%H:%M:%S.%fZ'
#     local_tz = pytz.timezone("Asia/Shanghai")
#     local_format = "%Y-%m-%d %H:%M:%S"
#     utc_dt = datetime.datetime.strptime(utc_time,utc_format)
#     local_dt= utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
#     local_s = local_dt.strftime(local_format)
#     print(local_s)
#
# utc_time = "2017-05-11T00:45:56.320Z"
# # utc_time= "'2017-05-11T00:45:56"
# utcform(utc_time)

# utc_time = "u'2017-05-11T00:45:56.223Z"
# if(utc_time.endswith("Z")):
# #     print(re.findall("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}",utc_time)[0])
# tt = "sfssdf"
# print(re.search("\d",tt))