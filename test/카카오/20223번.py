import datetime


def solution(fees, records):
    answer = []
    parking = {}
    tmp = {}
    for i in records:
        time, car_num, action = i.split(" ")
        if car_num not in parking:
            parking[car_num] = []

        if action == "IN":
            parking[car_num].append(time)
        else:
            in_time = parking[car_num][0]
            total = calculateParkingHour(in_time, time) # out일 때 총 주차 시간
            parking[car_num] = []
            if car_num not in tmp:
                tmp[car_num] = total
            else:
                tmp[car_num] += total

    for i in parking:
        if len(parking[i]) != 0:
            total = calculateParkingHour(parking[i][0], "23:59")
            if i not in tmp:
                tmp[i] = total
            else:
                tmp[i] += total

    tmp2 = []
    for i in tmp:
        time = tmp[i] - fees[0]
        if time < 0:
            time = 0
        if time%fees[2] != 0:
            final_time = time//fees[2] + 1
        else:
            final_time = time//fees[2]

        tmp2.append((i, final_time * fees[3] + fees[1]))

    tmp2 = sorted(tmp2)
    for i in tmp2:
        answer.append(i[1])

    return answer


def calculateParkingHour(in_time:str, out_time:str):
    in_hour, in_minute = in_time.split(":")
    out_hour, out_minute = out_time.split(":")
    parking_in = datetime.datetime(2022,11,13,int(in_hour),int(in_minute))
    parking_out = datetime.datetime(2022,11,13,int(out_hour), int(out_minute))


    total = (parking_out - parking_in).seconds
    return total//60



fees = [180, 5000, 10, 600] # 기본시간, 기본 요금, 단위시간, 단위요금
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
           "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
