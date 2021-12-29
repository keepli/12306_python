import urllib.request
import json

url = 'http://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-01-12&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=ICQ&purpose_codes=ADULT'

headers = {
    'Cookie':'_uab_collina=164078611867403942182275; JSESSIONID=F28AC4E5BDC7112DAF4002F69E13FA07; BIGipServerotn=1641611530.64545.0000; BIGipServerpassport=820510986.50215.0000; RAIL_EXPIRATION=1641055928318; RAIL_DEVICEID=WmuZ956NDYnQZPeI4ucTDm7_xlrHaSHg1KBcloyrdlb-n25E30ZyoAgQlHWKAtVUX0RzrBxB6Nu74zGPAizJuG067DdEok3w94aAWp8EgMmKXT8ggKU2Azv8VBo64juDvn81LAS403wrAckY2rm-M45D15deyu6K; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=495c805987d0f5c8c84b14f60212447d; _jc_save_fromStation=%u5E7F%u5DDE%2CGZQ; _jc_save_toStation=%u90F4%u5DDE%u897F%2CICQ; _jc_save_toDate=2021-12-29; _jc_save_wfdc_flag=dc; BIGipServerportal=3134456074.17695.0000; _jc_save_fromDate=2022-01-12',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
print(response)
content = response.read().decode('utf-8')

print(type(content))
print(content)

js = json.loads(content)
print(type(js))
print(js)

print(js['data']['result'])
