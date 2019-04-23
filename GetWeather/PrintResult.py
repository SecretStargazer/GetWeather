from prettytable import PrettyTable
import dateutil.parser

def printTencentWeatherForcast1H(result_data):
    pt = PrettyTable()
    ptHeader = '时间 温度 天气 风向 风力'.split(' ')
    pt._set_field_names(ptHeader)
    for i in range(len(result_data)):
        data = []
        data.append(dateutil.parser.parse(result_data[str(i)].get('update_time')))
        data.append(result_data[str(i)].get('degree'))
        data.append(result_data[str(i)].get('weather'))
        data.append(result_data[str(i)].get('wind_direction'))
        data.append(result_data[str(i)].get('wind_power'))
        i+=1
        if(len(data) == len(ptHeader)):
            pt.add_row(data)
    print(pt)

def printTencentWeatherForcast24H(result_data):
    pt = PrettyTable()
    ptHeader = '日期 最高温度 最低温度 白天天气 白天风向 白天风力 夜间天气 夜间风向 夜间风力'.split(' ')
    pt._set_field_names(ptHeader)
    for i in range(len(result_data)):
        data = []
        data.append(result_data[str(i)].get('time'))
        data.append(result_data[str(i)].get('max_degree'))
        data.append(result_data[str(i)].get('min_degree'))
        data.append(result_data[str(i)].get('day_weather'))
        data.append(result_data[str(i)].get('day_wind_direction'))
        data.append(result_data[str(i)].get('day_wind_power'))
        data.append(result_data[str(i)].get('night_weather'))
        data.append(result_data[str(i)].get('night_wind_direction'))
        data.append(result_data[str(i)].get('night_wind_power'))
        i+=1
        if(len(data) == len(ptHeader)):
            pt.add_row(data)
    print(pt)
