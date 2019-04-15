import GetWeatherFormTencentWeather as TencentWeather

def test_1():
    province,city = TencentWeather.getLocal()
    d = TencentWeather.getWeather('forecast_24h',province,city)
    print(d)