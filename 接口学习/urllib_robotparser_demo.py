#-*- coding:utf-8 -*-


__author__ = "苦叶子"


import urllib.robotparser

if __name__ == "__main__":
    print("robots.txt文件解析")

    r = urllib.robotparser.RobotFileParser()

    r.set_url("http://www.musi-cal.com/robots.txt")

    r.read()
    
    rrate = r.request_rate("*")

    print(rrate)