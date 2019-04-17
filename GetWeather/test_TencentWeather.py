import GetWeatherFormTencentWeather as TencentWeather
import PrintResult

def test_1h():
    province,city = TencentWeather.getLocal()
    data = TencentWeather.getWeather('forecast_1h',province,city)
    PrintResult.printTencentWeatherForcast1H(data)

def test_24h():
    province,city = TencentWeather.getLocal()
    data = TencentWeather.getWeather('forecast_24h',province,city)
    PrintResult.printTencentWeatherForcast24H(data)



