import urllib.request
import json

url = 'http://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-01-12&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=ICQ&purpose_codes=ADULT'

headers = {
    'Cookie':'_jc_save_fromStation=%u5E7F%u5DDE%2CGZQ; _jc_save_toStation=%u90F4%u5DDE%u897F%2CICQ; _jc_save_toDate=2021-12-29; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2022-01-12',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
print(response)
content = response.read().decode('utf-8')

print(type(content))
print(content)

js = json.loads(content)
result = js['data']['result']

print(result)
print(type(js['data']['result']))

for r in result:

    r_list = r.split("|")

