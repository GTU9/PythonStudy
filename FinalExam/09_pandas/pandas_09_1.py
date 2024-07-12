#데이터 수집,정리
import csv
with open("weather_data.csv") as data_file:
    # data=data_file.readlines()
    data=csv.reader(data_file)
    # print(data)
    tempeture=[]
    for row in data:
        # print(row)
        if row[1] !="temp":
            tempeture.append(row[1])
    # print(tempeture)

#데이터 가져오기
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)

#데이터프레임 딕셔너리 저장
data_dict=data.to_dict()
# print(data_dict)

#데이터프레임 리스트 저장
temp_list=data["temp"].to_list()
# print(temp_list)

#평균 온도 계산
avg=sum(temp_list)/len(temp_list)
# print(avg)
# print(data["temp"].mean())

# print(data["temp"].max()) #최댓값
# print(data["temp"].min()) #최솟값
# print(data.temp.median()) #중간값

#금요일의 온도 상태
# print(data[data["day"]=="Friday"])

#온도가 가장 높은 요일의 상태
# print(data[data["temp"].max()==data["temp"]])

#월요일의 온도를 화씨로 변경해서 출력 ℉=(℃×9/5​)+32
monday=data[data["day"]=="Monday"]
monday_temp=int(monday["temp"])
monday_temp_f=(monday_temp*9/5)+32
# print(monday_temp_f)

#딕셔너리를 데이터프레임으로 변경하기

new_data = {
    'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'temp': [24, 26, 22, 29, 21, 25, 28],
    'condition': ['Sunny', 'Cloudy', 'Rainy', 'Windy', 'Sunny', 'Cloudy', 'Rainy']
}

weather_data = pandas.DataFrame(new_data)
# weather_data.to_csv("new_data.csv")
