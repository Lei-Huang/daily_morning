import requests
import math
from datetime import datetime

def get_weather():
    url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=堪培拉"
    res = requests.get(url).json()
    weather = res['data']['list'][0]
    return (weather['weather'], math.floor(weather['temp']), weather['humidity'], math.floor(weather['low']), math.floor(weather['high']), weather['wind'])

wea, temperature, humidity, low, high, wind = get_weather()
data = {"weather":{"value":wea},"temperature":{"value":temperature},"humidity":{"value":humidity},"low_temp":{"value":low},"high_temp":{"value":high},"wind":{"value":wind}}

def get_words():
    dateTimeObj = datetime.now()
    if(dateTimeObj.hour == 8):
        words = requests.get("http://api.tianapi.com/star/index?key=419186fbca431df736e8a80f9bdcadca&astro=virgo").json()
        return words['newslist'][-1]['content']
    if (dateTimeObj.hour == 10):
        words = requests.get("http://api.tianapi.com/qingshi/index?key=419186fbca431df736e8a80f9bdcadca").json()
        return words['newslist'][-1]['content'] + " " + words['newslist'][-1]['source'] + " " + words['newslist'][-1][
            'author']
    if (dateTimeObj.hour == 14):
        words = requests.get("http://api.tianapi.com/zmsc/index?key=419186fbca431df736e8a80f9bdcadca").json()
        return words['newslist'][-1]['content'] + " " + words['newslist'][-1]['source']
    words = requests.get("http://api.tianapi.com/dialogue/index?key=419186fbca431df736e8a80f9bdcadca").json()
    return words['newslist'][-1]['dialogue'] + " " +words['newslist'][-1]['english'] +"-" + words['newslist'][-1]['source']

print(get_words())