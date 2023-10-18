# coding=cp950
import requests
import config

def notify(msg):
    token_key = config.LineNotifyToken
    header = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":'Bearer '+token_key}
    URL = 'https://notify-api.line.me/api/notify'
    payload = {'message':msg}
    res=requests.post(URL,headers=header,data=payload)

if __name__ == '__main__':
    msg = '中文cp950'
    notify(msg)
