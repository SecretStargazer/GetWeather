import requests
import urllib
import pandas
import datetime
import json

def getLocal():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    url = "https://apis.map.qq.com/ws/location/v1/ip?key=3BFBZ-ZKD3X-LW54A-ZT76D-E7AHO-4RBD5&&output=jsonp&callback=jQuery1113032646423270200886_1554795513443&_=1554795513444"    
    web_data = requests.get(url, headers=header)
    web_data.encoding = 'utf-8'
    startPos = web_data.text.index('{')
    datas = json.loads(web_data.text[startPos:-1])
    province = datas['result']['ad_info']['province']
    city = datas['result']['ad_info']['city']
    return province,city

def getWeather(province=getLocal()[0],city=getLocal()[1]):
    provinceURL = urllib.parse.quote(province)
    cityURL = urllib.parse.quote(city)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    url = "https://wis.qq.com/weather/common?source=pc&weather_type=observe%7Cforecast_1h%7Cforecast_24h%7Cindex%7Calarm%7Climit%7Ctips%7Crise&province={0}&city={1}&county=&callback=jQuery111303041900138614775_1554708929049&_=1554708929050".format(provinceURL  , cityURL)    
    web_data = requests.get(url, headers=header)
    web_data.encoding = 'utf-8'
    startPos = web_data.text.index('{')
    datas = json.loads(web_data.text[startPos:-1])
    result_data = datas['data']
    print(datas['data']['forecast_1h'])
    return result_data

if __name__ == "__main__":
    province,city = getLocal()
    getWeather(province,city)
