import requests
import math
def get_weather():
    url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=堪培拉"
    res = requests.get(url).json()
    weather = res['data']['list'][0]
    return (weather['weather'], math.floor(weather['temp']), weather['humidity'], math.floor(weather['low']), math.floor(weather['high']), weather['wind'])

wea, temperature, humidity, low, high, wind = get_weather()
data = {"weather":{"value":wea},"temperature":{"value":temperature},"humidity":{"value":humidity},"low_temp":{"value":low},"high_temp":{"value":high},"wind":{"value":wind}}


def get_words():
    words = requests.get("http://api.tianapi.com/star/index?key=419186fbca431df736e8a80f9bdcadca&astro=virgo").json()
    return words['newslist'][-1]['content']

print(get_words())